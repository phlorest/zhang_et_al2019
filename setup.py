from setuptools import setup


setup(
    name='cldfbench_zhang_et_al2019',
    py_modules=['cldfbench_zhang_et_al2019'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'zhang_et_al2019=cldfbench_zhang_et_al2019:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
