from setuptools import setup, find_packages
setup(
	name='Salesman_App',
	version=version,
	description='Frappe application to manage the manufacturing workflows in the garment industry.',
	author='ash',
	author_email='ash67fm@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
