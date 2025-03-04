reference_codes = [
    """
    #include <stdio.h>
    #include <string.h>

    void vulnerable_function(char *input) {
        char buffer[50];  // Small buffer size
        strcpy(buffer, input);  // No bounds checking
        printf("You entered: %s\n", buffer);
    }

    int main(int argc, char *argv[]) {
        if (argc > 1) {
            vulnerable_function(argv[1]);  // Passes user input directly
        } else {
            printf("Usage: %s <input>\n", argv[0]);
        }
        return 0;
    }
    // Exploitation: Buffer Overflow attack possible.
    """,

    """
    #include <stdio.h>
    #include <stdlib.h>

    int main() {
        char *ptr = (char *)malloc(20);
        strcpy(ptr, "Use After Free!");
        free(ptr);  // Memory is freed

        printf("%s\n", ptr);  // Dangling pointer usage
        return 0;
    }
    // Exploitation: Use-After-Free leading to arbitrary code execution.
    """,

    """
    #include <stdio.h>
    #include <string.h>

    void exploit_me() {
        char buffer[32];
        gets(buffer);  // Dangerous function - No bounds checking
        printf("Received input: %s\n", buffer);
    }

    int main() {
        exploit_me();
        return 0;
    }
    // Exploitation: Stack-based buffer overflow.
    """,

    """
    #include <stdio.h>
    #include <stdlib.h>
    #include <unistd.h>
    #include <fcntl.h>

    #define FILE_NAME "/tmp/vulnerable.txt"

    void create_file() {
        int fd = open(FILE_NAME, O_WRONLY | O_CREAT, 0644);
        if (fd < 0) {
            perror("File open failed");
            exit(1);
        }
        sleep(5);  // Simulate a delay before writing
        write(fd, "This is a secret file\n", 22);
        close(fd);
    }

    int main() {
        create_file();
        return 0;
    }
    // Exploitation: Race Condition via symbolic links.
    """,

    """
    #include <stdio.h>
    #include <stdlib.h>

    void read_file(char *filename) {
        char path[100];
        snprintf(path, sizeof(path), "/var/data/%s", filename);
        FILE *file = fopen(path, "r");
        if (file) {
            char buffer[256];
            while (fgets(buffer, sizeof(buffer), file)) {
                printf("%s", buffer);
            }
            fclose(file);
        } else {
            printf("Error opening file.\n");
        }
    }

    int main(int argc, char *argv[]) {
        if (argc > 1) {
            read_file(argv[1]);  // User-controlled input
        } else {
            printf("Usage: %s <filename>\n", argv[0]);
        }
        return 0;
    }
    // Exploitation: Directory Traversal Attack.
    """,

    """
    #include <stdio.h>
    #include <sqlite3.h>

    void execute_query(char *user_input) {
        sqlite3 *db;
        sqlite3_open("test.db", &db);
        char query[256];

        snprintf(query, sizeof(query), "SELECT * FROM users WHERE username='%s';", user_input);
        printf("Executing: %s\n", query);

        sqlite3_exec(db, query, NULL, NULL, NULL);
        sqlite3_close(db);
    }

    int main(int argc, char *argv[]) {
        if (argc > 1) {
            execute_query(argv[1]);  // User-controlled SQL input
        } else {
            printf("Usage: %s <username>\n", argv[0]);
        }
        return 0;
    }
    // Exploitation: SQL Injection (e.g., "admin' --").
    """,

    """
    <!DOCTYPE html>
    <html>
    <head><title>XSS Example</title></head>
    <body>
        <form action="xss.html" method="GET">
            <input type="text" name="msg">
            <input type="submit" value="Submit">
        </form>

        <script>
            const urlParams = new URLSearchParams(window.location.search);
            document.write("Message: " + urlParams.get("msg"));
        </script>
    </body>
    </html>
    // Exploitation: Cross-Site Scripting (XSS).
    """,

    """
    const express = require('express');
    const app = express();

    app.use(express.urlencoded({ extended: true }));

    app.get('/', (req, res) => {
        res.send(`<h1>Welcome</h1><p>${req.query.name}</p>`);
    });

    app.listen(3000, () => {
        console.log('Server running on http://localhost:3000');
    });
    // Exploitation: XSS via URL query parameters.
    """,

    """
    #include <stdio.h>

    void vulnerable_function(char *input) {
        printf(input);  // Unsanitized user input used directly
    }

    int main(int argc, char *argv[]) {
        if (argc > 1) {
            vulnerable_function(argv[1]);  
        } else {
            printf("Usage: %s <input>\n", argv[0]);
        }
        return 0;
    }
    // Exploitation: Format String Vulnerability.
    """,

    """
    #include <stdio.h>
    #include <stdlib.h>

    void execute_command(char *input) {
        char command[100];
        snprintf(command, sizeof(command), "ls %s", input);
        system(command);  // Dangerous function
    }

    int main(int argc, char *argv[]) {
        if (argc > 1) {
            execute_command(argv[1]);
        } else {
            printf("Usage: %s <directory>\n", argv[0]);
        }
        return 0;
    }
    // Exploitation: Command Injection.
    """
]
