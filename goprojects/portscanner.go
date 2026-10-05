package main

import (
	"flag"
	"fmt"
	"net"
	"strconv"
	"sync"
	"time"
)

func scanPort(host string, port int, wg *sync.WaitGroup) {
	defer wg.Done() // tell WaitGroup this goroutine is done

	address := host + ":" + strconv.Itoa(port)
	conn, err := net.DialTimeout("tcp", address, 500*time.Millisecond)
	if err == nil {
		fmt.Printf("port %d is OPEN\n", port)
		conn.Close()
	}
}

func main() {
	host := flag.String("host", "", "Host to scan (e.g. 127.0.0.1 or scanme.nmap.org)")
	startPort := flag.Int("start", 1, "Start port number")
	endPort := flag.Int("end", 1024, "End port number")
	flag.Parse()

	// Check if host is empty
	if *host == "" {
		fmt.Println("please provide a host using --host")
		return
	}

	fmt.Printf("scanning %s from port %d to %d...\n", *host, *startPort, *endPort)

	var wg sync.WaitGroup

	for port := *startPort; port <= *endPort; port++ {
		wg.Add(1)
		go scanPort(*host, port, &wg)
	}

	wg.Wait()
	fmt.Println("scan complete.")
}
