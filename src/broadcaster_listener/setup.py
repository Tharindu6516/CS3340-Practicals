import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'broadcaster_listener'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tharindu',
    maintainer_email='tharindu@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dynamic_frame_tf2_broadcaster = broadcaster_listener.dynamic_frame_tf2_broadcaster:main',
            'fixed_frame_tf2_broadcaster = broadcaster_listener.fixed_frame_tf2_broadcaster:main',
            'turtle_tf2_broadcaster = broadcaster_listener.turtle_tf2_broadcaster:main',
            'turtle_tf2_listener = broadcaster_listener.turtle_tf2_listener:main',
        ],
    },
)
