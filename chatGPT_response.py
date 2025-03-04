vulnerable_codes = [ # 1. Buffer Overflow Vulnerable C Program '''#include <stdio.h> #include <string.h>

void vulnerable_function(char *input) { char buffer[50]; strcpy(buffer, input); // No bounds checking: vulnerable to buffer overflow }

int main() { char large_input[] = "A very long input that will overflow the buffer and cause undefined behavior!"; vulnerable_function(large_input); // This overflows the buffer return 0; }''',

# 2. Use-After-Free Vulnerability in C
'''#include <stdio.h>
#include <stdlib.h>

void vulnerable_function() { char *buffer = (char *)malloc(100); strcpy(buffer, "Sensitive data stored here."); printf("Buffer content: %s\n", buffer);

// Free the allocated memory
free(buffer);

// Use-after-free: Accessing the memory after it has been freed
printf("Buffer content after free: %s\n", buffer);  // Undefined behavior
}

int main() { vulnerable_function(); return 0; }''',

# 3. Stack-Based Buffer Overflow Vulnerability in C
'''#include <stdio.h>
#include <string.h>

void vulnerable_function(char *input) { char buffer[100]; // No bounds checking: susceptible to stack-based buffer overflow strcpy(buffer, input); // Overflow here }

int main() { char large_input[] = "This is a very long input string that will overflow the buffer and potentially overwrite the return address!"; vulnerable_function(large_input); // Overflow will cause crash or unexpected behavior return 0; }''',

# 4. Race Condition Vulnerability in C
'''#include <stdio.h>
#include <stdlib.h> #include <pthread.h> #include <unistd.h>

int shared_resource = 0;

void *increment_resource(void *arg) { int i; for (i = 0; i < 100000; i++) { shared_resource++; // Race condition: no synchronization } return NULL; }

int main() { pthread_t thread1, thread2; pthread_create(&thread1, NULL, increment_resource, NULL); pthread_create(&thread2, NULL, increment_resource, NULL);

pthread_join(thread1, NULL);
pthread_join(thread2, NULL);

printf("Final shared resource value: %d\n", shared_resource);  // The value may not be what we expect due to race condition
return 0;
}''',

# 5. Insecure File Handling (Directory Traversal) Vulnerability in C
'''#include <stdio.h>
#include <stdlib.h>

void vulnerable_function(char *filename) { FILE *file;

// Insecure file handling: the user can control the filename and perform directory traversal
file = fopen(filename, "r");
if (file == NULL) {
    printf("Error opening file!\n");
    return;
}

char buffer[100];
fgets(buffer, 100, file);
printf("File content: %s\n", buffer);
fclose(file);
}

int main() { char user_input[100]; printf("Enter a filename: "); scanf("%s", user_input); // User can specify files outside the intended directory

vulnerable_function(user_input);  // If the input is something like "../etc/passwd", it will access sensitive files
return 0;
}''',

# 6. SQL Injection Vulnerability in C
'''#include <stdio.h>
#include <string.h> #include <mysql/mysql.h>

void vulnerable_sql_query(char *user_input) { MYSQL *conn; MYSQL_RES *res; MYSQL_ROW row;

conn = mysql_init(NULL);
if (conn == NULL) {
    fprintf(stderr, "mysql_init() failed\n");
    exit(1);
}

if (mysql_real_connect(conn, "localhost", "user", "password", "database", 0, NULL, 0) == NULL) {
    fprintf(stderr, "mysql_real_connect() failed\n");
    exit(1);
}

char query[256];
snprintf(query, sizeof(query), "SELECT * FROM users WHERE username='%s'", user_input);  // Vulnerable to SQL Injection
if (mysql_query(conn, query)) {
    fprintf(stderr, "SELECT * FROM users failed. Error: %s\n", mysql_error(conn));
    exit(1);
}

res = mysql_store_result(conn);
if (res == NULL) {
    fprintf(stderr, "mysql_store_result() failed. Error: %s\n", mysql_error(conn));
    exit(1);
}

while ((row = mysql_fetch_row(res)) != NULL) {
    printf("%s\n", row[0]);  // Output user details
}

mysql_free_result(res);
mysql_close(conn);
}

int main() { char user_input[100]; printf("Enter your username: "); scanf("%s", user_input); // User input directly placed into SQL query

vulnerable_sql_query(user_input);  // This could allow SQL injection
return 0;
}''',

# 7. JavaScript Cross-Site Scripting (XSS) Vulnerability
'''<!DOCTYPE html>
<title>Cross-Site Scripting (XSS) Example</title>
Welcome to our website
Username: Submit
<p>Your username: <span id="username_display"></span></p>

<script>
    // This is a vulnerable JavaScript code susceptible to XSS
    const urlParams = new URLSearchParams(window.location.search);
    const username = urlParams.get('username');
    document.getElementById('username_display').innerHTML = username;  // Vulnerable to XSS if username contains malicious script
</script>
''',
# 8. Vulnerable JavaScript Code Exploitable by XSS Attack
'''<!DOCTYPE html>
<title>Vulnerable JavaScript XSS Example</title>
