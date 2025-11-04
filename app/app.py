from flask import Flask, render_template_string, request
app = Flask(__name__)

code_snippets = {
    "reverse_string": {
        "logic": "Take a string input Mayur and print it backwards using a loop or recursion.",
        "easy": r"""#include <stdio.h>
#include <string.h>

int main() {
    char s[100];
    printf("Enter a string: ");
    gets(s);

    printf("Reversed string: ");
    for (int i = strlen(s) - 1; i >= 0; i--)
        printf("%c", s[i]);
    return 0;
}
""",
        "advanced": r"""#include <stdio.h>
#include <string.h>

void rev(char *s, int a, int b) {
    if (a >= b) return;
    char t = s[a];
    s[a] = s[b];
    s[b] = t;
    rev(s, a + 1, b - 1);
}

int main() {
    char s[100];
    printf("Enter a string: ");
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;
    rev(s, 0, strlen(s) - 1);
    printf("Reversed string: %s\n", s);
    return 0;
}
"""
    },

    "palindrome": {
        "logic": "Compare first and last characters of a string moving inward; if all match, it’s a palindrome.",
        "easy": r"""#include <stdio.h>
#include <string.h>

int main() {
    char s[100];
    printf("Enter a string: ");
    gets(s);
    int len = strlen(s), flag = 0;
    for (int i = 0; i < len / 2; i++) {
        if (s[i] != s[len - i - 1]) {
            flag = 1;
            break;
        }
    }
    if (flag == 0)
        printf("Palindrome\n");
    else
        printf("Not a palindrome\n");
    return 0;
}
""",
        "advanced": r"""#include <stdio.h>
#include <string.h>
#include <ctype.h>

int isPalindrome(const char *s) {
    int l = 0, r = strlen(s) - 1;
    while (l < r) {
        while (!isalnum(s[l])) l++;
        while (!isalnum(s[r])) r--;
        if (tolower(s[l++]) != tolower(s[r--])) return 0;
    }
    return 1;
}

int main() {
    char s[100];
    printf("Enter a string: ");
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;
    printf("%s\n", isPalindrome(s) ? "Palindrome" : "Not a palindrome");
    return 0;
}
"""
    },

    "factorial": {
        "logic": "Multiply all integers from 1 to n. Can be done iteratively or recursively with input validation.",
        "easy": r"""#include <stdio.h>

int main() {
    int n, fact = 1;
    printf("Enter a number: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
        fact *= i;

    printf("Factorial = %d\n", fact);
    return 0;
}
""",
        "advanced": r"""#include <stdio.h>

long long factorial(int n) {
    if (n < 0) return -1;
    return (n <= 1) ? 1 : n * factorial(n - 1);
}

int main() {
    int n;
    printf("Enter a number: ");
    if (scanf("%d", &n) != 1 || n < 0) {
        printf("Invalid input!\n");
        return 1;
    }
    printf("Factorial = %lld\n", factorial(n));
    return 0;
}
"""
    },

    "fibonacci": {
        "logic": "Generate Fibonacci numbers starting from 0 and 1, either iteratively or recursively.",
        "easy": r"""#include <stdio.h>

int main() {
    int n, a = 0, b = 1, next;
    printf("Enter number of terms: ");
    scanf("%d", &n);

    printf("Fibonacci Series: ");
    for (int i = 1; i <= n; i++) {
        printf("%d ", a);
        next = a + b;
        a = b;
        b = next;
    }
    printf("\n");
    return 0;
}
""",
        "advanced": r"""#include <stdio.h>

void fibonacci(int n, int a, int b) {
    if (n == 0) return;
    printf("%d ", a);
    fibonacci(n - 1, b, a + b);
}

int main() {
    int n;
    printf("Enter number of terms: ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Invalid input!\n");
        return 1;
    }
    printf("Fibonacci Series: ");
    fibonacci(n, 0, 1);
    printf("\n");
    return 0;
}
"""
    }
}

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<style>
body { font-family: Arial; background:#f4f4f4; padding:20px;}
pre { background:#222; color:#0f0; padding:10px; border-radius:8px; white-space:pre-wrap;}
.logic { background:#fff3cd; padding:10px; border-left:5px solid #ffc107; border-radius:6px; color:#333;}
.btn { background:#007bff; color:white; padding:8px 12px; border:none; border-radius:4px; cursor:pointer;}
.btn:hover{background:#0056b3;}
</style>
</head>
<body>
<h1>C Programming Logic Examples</h1>
<form method="get" action="/">
  <button class="btn" name="code" value="reverse_string">Reverse String</button>
  <button class="btn" name="code" value="palindrome">Palindrome</button>
  <button class="btn" name="code" value="factorial">Factorial</button>
  <button class="btn" name="code" value="fibonacci">Fibonacci</button>
</form>
{% if selected %}
  <h2>{{ selected.replace('_', ' ').title() }}</h2>
  <h3>🧠 Logic</h3>
  <div class="logic">{{ logic }}</div>
  <h3>💡 Easy Version</h3>
  <pre>{{ easy }}</pre>
  <h3>⚙️ Advanced Version</h3>
  <pre>{{ advanced }}</pre>
{% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def menu():
    sel = request.args.get("code")
    if sel and sel in code_snippets:
        data = code_snippets[sel]
        return render_template_string(
            TEMPLATE,
            selected=sel,
            logic=data["logic"],
            easy=data["easy"],
            advanced=data["advanced"]
        )
    return render_template_string(TEMPLATE, selected=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

