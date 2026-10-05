package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
)

func main() {
	// Serve static files (HTML, CSS, JS)
	fs := http.FileServer(http.Dir("./static"))
	http.Handle("/", fs)

	// Serve uploaded images
	http.Handle("/uploads/", http.StripPrefix("/uploads/", http.FileServer(http.Dir("./uploads"))))

	// Handle upload and gallery
	http.HandleFunc("/upload", uploadHandler)
	http.HandleFunc("/gallery", galleryHandler)

	log.Println("🚀 Server started at http://localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func uploadHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}

	err := r.ParseMultipartForm(10 << 20)
	if err != nil {
		http.Error(w, "Error parsing form", http.StatusBadRequest)
		return
	}

	username := r.FormValue("username")
	if username == "" {
		http.Error(w, "Username is required", http.StatusBadRequest)
		return
	}

	file, handler, err := r.FormFile("image")
	if err != nil {
		http.Error(w, "Error retrieving file", http.StatusBadRequest)
		return
	}
	defer file.Close()

	userFolder := fmt.Sprintf("./uploads/%s", username)
	os.MkdirAll(userFolder, os.ModePerm)

	dst, err := os.Create(userFolder + "/" + handler.Filename)
	if err != nil {
		http.Error(w, "Error saving file", http.StatusInternalServerError)
		return
	}
	defer dst.Close()

	_, err = io.Copy(dst, file)
	if err != nil {
		http.Error(w, "Error writing file", http.StatusInternalServerError)
		return
	}

	fmt.Fprintf(w, "Uploaded successfully: %s", handler.Filename)
}

func galleryHandler(w http.ResponseWriter, r *http.Request) {
	user := r.URL.Query().Get("user")
	if user == "" {
		http.Error(w, "Missing user", http.StatusBadRequest)
		return
	}

	userFolder := "./uploads/" + user
	files, err := os.ReadDir(userFolder)
	if err != nil {
		http.Error(w, "Cannot read user folder", http.StatusInternalServerError)
		return
	}

	var filenames []string
	for _, file := range files {
		if !file.IsDir() {
			filenames = append(filenames, file.Name())
		}
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(filenames)
}
