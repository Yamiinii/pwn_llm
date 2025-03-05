generated_codes = [
    """#include <stdio.h>
#include <string.h>

void vulnerable_function() {
    char buffer[16];
    printf("Enter input: ");
    gets(buffer);  // Unsafe function prone to buffer overflow
}

int main() {
    vulnerable_function();
    return 0;
}""",

    """#include <stdlib.h>
#include <stdio.h>

int main() {
    char *ptr = malloc(10);
    free(ptr);
    printf("%s", ptr);  // Accessing freed memory
    return 0;
}""",

    """#include <stdio.h>
#include <string.h>

void vulnerable_function() {
    char buffer[16];
    printf("Enter input: ");
    gets(buffer);  // Unsafe function prone to buffer overflow
}

int main() {
    vulnerable_function();
    return 0;
}""",

    """#include <stdlib.h>
#include <stdio.h>

int main() {
    char *ptr = malloc(10);
    free(ptr);
    printf("%s", ptr);  // Accessing freed memory
    return 0;
}""",

    """#include <stdio.h>

void vulnerable_function() {
    char buffer[10];
    printf("Enter input: ");
    gets(buffer);  // Unsafe function, prone to stack-based buffer overflow
}

int main() {
    vulnerable_function();
    return 0;
}""",

    """#include <pthread.h>
#include <stdio.h>

int counter = 0;

void* increment() {
    for(int i = 0; i < 1000; i++) counter++;  // Race condition, as there is no synchronization
}

int main() {
    pthread_t t1, t2;
    pthread_create(&t1, NULL, increment, NULL);
    pthread_create(&t2, NULL, increment, NULL);
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    printf("Counter: %d\n", counter);  // Race condition vulnerability
    return 0;
}""",

    """#include <stdio.h>

int main(int argc, char *argv[]) {
    FILE *file = fopen(argv[1], "r");  // Insecure file handling, vulnerable to directory traversal
    char content[256];
    fread(content, 1, sizeof(content), file);
    printf("%s", content);
    fclose(file);
    return 0;
}""",

    """#include <stdio.h>
#include <string.h>

void login(char *username, char *password) {
    char query[256];
    sprintf(query, "SELECT * FROM users WHERE username='%s' AND password='%s'", username, password);  // Vulnerable to SQL injection
    printf("Executing query: %s\n", query);
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <username> <password>\n", argv[0]);
        return 1;
    }
    login(argv[1], argv[2]);
    return 0;
}""",

    """<input type="text" id="comment" onblur="document.write(this.value)">  <!-- XSS vulnerability -->""",

    """<input type="text" id="input" onblur="document.write(this.value)">  <!-- XSS vulnerability -->"""
]

