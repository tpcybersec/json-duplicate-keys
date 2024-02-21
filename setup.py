import setuptools

setuptools.setup(
	name="json-duplicate-keys",
	version="2024.2.21",
	author="TP Cyber Security",
	license="MIT",
	author_email="tpcybersec2023@gmail.com",
	description="Flatten/ Unflatten and Load(s)/ Dump(s) JSON File/ Object with Duplicate Keys",
	long_description=open("README.md").read(),
	long_description_content_type="text/markdown",
	install_requires=open("requirements.txt").read().split(),
	url="https://github.com/truocphan/json-duplicate-keys",
	classifiers=[
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 2",
		"Programming Language :: Python :: Implementation :: Jython"
	],
	keywords=["TPCyberSec", "json", "duplicate keys", "json duplicate keys", "flatten", "unflatten"],
	packages=["json_duplicate_keys"],
)