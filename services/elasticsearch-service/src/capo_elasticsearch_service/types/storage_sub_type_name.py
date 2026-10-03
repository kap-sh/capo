"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#StorageSubTypeName``."""

from typing import TypeAlias

"""<p> SubType of the given storage type. List of available sub-storage options: For "instance" storageType we wont have any storageSubType, in case of "ebs" storageType we will have following valid storageSubTypes <ol> <li>standard</li> <li>gp2</li> <li>gp3</li> <li>io1</li> </ol> Refer <code><a>VolumeType</a></code> for more information regarding above EBS storage options. </p>"""
StorageSubTypeName: TypeAlias = str
