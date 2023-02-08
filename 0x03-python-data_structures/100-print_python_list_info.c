/**
 * print_python_list_info - A C function that prints
 *		some basic info about Python lists.
 * @p: Py Object to be printed
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyListObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	print("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
