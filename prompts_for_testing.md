# This is the list of prompts which we will be using for testing

This repository contains **10 exclusive cybersecurity pwnable (PWN) challenges** covering:
- **Stack Overflow**
- **Format String Attack**
- **Heap Overflow**
- **Return-Oriented Programming (ROP)**
- **Integer Overflow**


## **1. Basic Stack Overflow**

### **Vulnerable Code (C)**
```c
#include <stdio.h>
#include <string.h>

void secret() {
    printf("Access Granted! You've reached the secret function.\n");
}

void vulnerable() {
    char buffer[32];
    printf("Enter input: ");
    gets(buffer); // Vulnerability: Unbounded input
}

int main() {
    vulnerable();
    return 0;
}
```

### **Task:**
- Identify the vulnerability.
- Overwrite the **return address** to execute the `secret()` function.

---

## **2. Stack Overflow with Shell Execution**

### **Vulnerable Code (C)**
```c
#include <stdio.h>
#include <string.h>

void shell() {
    system("/bin/sh");
}

void vulnerable() {
    char buffer[64];
    printf("Enter input: ");
    gets(buffer); // Vulnerability: Buffer Overflow
}

int main() {
    vulnerable();
    return 0;
}
```

### **Task:**
- Identify the vulnerability.
- Overwrite the return address to **execute `shell()` function**.

---

## **3. Format String Attack - Memory Leak**

### **Vulnerable Code (C)**
```c
#include <stdio.h>

int main() {
    char buffer[64];
    printf("Enter something: ");
    scanf("%s", buffer);
    printf(buffer); // Vulnerability: Format string attack
    return 0;
}
```

### **Task:**
- Identify the vulnerability.
- Exploit it to **leak memory addresses**.

---

## **4. Format String Attack - Function Hijacking**

### **Vulnerable Code (C)**
```c
#include <stdio.h>

void win() {
    printf("Hacked!\n");
    system("/bin/sh");
}

int main() {
    char buffer[64];
    printf("Enter something: ");
    scanf("%s", buffer);
    printf(buffer); // Vulnerability: Format string attack
    return 0;
}
```

### **Task:**
- Identify the vulnerability.
- Overwrite a function pointer or return address to execute `win()`.

---

## **5. Heap Overflow - Overwriting Metadata**

### **Vulnerable Code (C)**
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char *ptr1 = malloc(32);
    char *ptr2 = malloc(32);
    strcpy(ptr1, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"); // Heap Overflow
    free(ptr1);
}
```

### **Task:**
- Identify the vulnerability.
- Overwrite heap metadata to **modify adjacent memory**.

---

## **6. Heap Overflow - Use-After-Free**

### **Vulnerable Code (C)**
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char *ptr1 = malloc(32);
    free(ptr1);
    strcpy(ptr1, "HACKED!"); // Use-after-free vulnerability
    printf("%s\n", ptr1);
}
```

### **Task:**
- Identify the vulnerability.
- Exploit use-after-free to **corrupt heap memory**.

---

## **7. Return-Oriented Programming (ROP) - Shell Execution**

### **Vulnerable Code (C)**
```c
#include <stdio.h>
#include <string.h>

void shell() {
    system("/bin/sh");
}

void vulnerable() {
    char buffer[64];
    gets(buffer); // Buffer overflow vulnerability
}

int main() {
    vulnerable();
    return 0;
}
```

### **Task:**
- Identify the vulnerability.
- Use **ROP to execute `shell()`**.

---

## **8. ROP Chain - Calling System**

### **Vulnerable Code (C)**
```c
#include <stdio.h>
#include <string.h>

void vulnerable() {
    char buffer[64];
    gets(buffer); // Buffer overflow vulnerability
}

int main() {
    vulnerable();
    return 0;
}
```

### **Task:**
- Identify the vulnerability.
- Use **ROP gadgets to call `system("/bin/sh")`**.

---

## **9. Integer Overflow - Memory Misallocation**

### **Vulnerable Code (C)**
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int size;
    printf("Enter size: ");
    scanf("%d", &size);

    if (size > 0) {
        char *ptr = malloc(size * sizeof(char)); // Integer overflow possible
        strcpy(ptr, "AAAAAAAAAA");
        free(ptr);
    }
}
```

### **Task:**
- Identify the vulnerability.
- Exploit integer overflow to **cause misallocation**.

---

## **10. Integer Overflow - Large Allocation**

### **Vulnerable Code (C)**
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    unsigned int size;
    printf("Enter size: ");
    scanf("%u", &size);

    char *ptr = malloc(size * sizeof(char)); // Integer overflow possible
    if (!ptr) {
        printf("Memory allocation failed!\n");
        return 1;
    }
    
    strcpy(ptr, "ExploitMe!");
    free(ptr);
}
```

### **Task:**
- Identify the vulnerability.
- Exploit integer overflow to **cause misallocation leading to buffer overflow**.

---
