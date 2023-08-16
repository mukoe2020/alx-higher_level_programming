#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;

    printf("[*] Python list info\n");
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; ++i) {
        PyObject *element = PyList_GetItem(p, i);
        printf("Element %ld: ", i);

        if (PyBytes_Check(element)) {
            printf("bytes\n");
            printf("[.] bytes object info\n");
            printf("  size: %ld\n", PyBytes_Size(element));

            if (PyBytes_Size(element) > 10) {
                printf("  trying string: %s\n", PyBytes_AsString(element));
                printf("  first 11 bytes: ");
                for (int j = 0; j < 10; ++j) {
                    printf("%02x ", (unsigned char)PyBytes_AsString(element)[j]);
                }
                printf("\n");
            } else {
                printf("  trying string: %s\n", PyBytes_AsString(element));
                printf("  first %ld bytes: ", PyBytes_Size(element));
                for (int j = 0; j < PyBytes_Size(element); ++j) {
                    printf("%02x ", (unsigned char)PyBytes_AsString(element)[j]);
                }
                printf("\n");
            }
        } else {
            printf("%s\n", Py_TYPE(element)->tp_name);
        }
    }
}

void print_python_bytes(PyObject *p) {
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyBytes_Size(p));

    if (PyBytes_Size(p) > 10) {
        printf("  trying string: %s\n", PyBytes_AsString(p));
        printf("  first 11 bytes: ");
        for (int i = 0; i < 10; ++i) {
            printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
        }
        printf("\n");
    } else {
        printf("  trying string: %s\n", PyBytes_AsString(p));
        printf("  first %ld bytes: ", PyBytes_Size(p));
        for (int i = 0; i < PyBytes_Size(p); ++i) {
            printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
        }
        printf("\n");
    }
}

int main(void) {
    return 0;
}
