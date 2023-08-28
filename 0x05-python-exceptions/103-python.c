#include <Python.h>

void print_python_list(PyObject *p) {
    if (PyList_Check(p)) {
        Py_ssize_t size = PyList_Size(p);
        Py_ssize_t i;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

        for (i = 0; i < size; i++) {
            PyObject *element = PyList_GetItem(p, i);
            printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
        }
    } else {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
    }
}

void print_python_bytes(PyObject *p) {
    if (PyBytes_Check(p)) {
        Py_ssize_t size = PyBytes_Size(p);
        char *str = PyBytes_AsString(p);
        int i;

        printf("[.] bytes object info\n");
        printf("  size: %ld\n", size);
        printf("  trying string: %s\n", str);
        printf("  first 10 bytes: ");
        for (i = 0; i < 10 && i < size; i++) {
            printf("%02x", (unsigned char)str[i]);
            if (i + 1 < size)
                printf(" ");
        }
        printf("\n");
    } else {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
    }
}

void print_python_float(PyObject *p) {
    if (PyFloat_Check(p)) {
        printf("[.] float object info\n");
        printf("  value: %f\n", PyFloat_AsDouble(p));
    } else {
        fprintf(stderr, "[ERROR] Invalid Float Object\n");
    }
}
