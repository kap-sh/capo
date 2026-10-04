"""Generated from Smithy shape ``com.amazonaws.s3#InventoryOptionalField``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

InventoryOptionalField: TypeAlias = Literal[
    "Size",
    "LastModifiedDate",
    "StorageClass",
    "ETag",
    "IsMultipartUploaded",
    "ReplicationStatus",
    "EncryptionStatus",
    "ObjectLockRetainUntilDate",
    "ObjectLockMode",
    "ObjectLockLegalHoldStatus",
    "ObjectLockEventHoldStatus",
    "ObjectLockEventHoldDuration",
    "IntelligentTieringAccessTier",
    "BucketKeyStatus",
    "ChecksumAlgorithm",
    "ObjectAccessControlList",
    "ObjectOwner",
    "LifecycleExpirationDate",
    "IntelligentTieringReferenceDate",
]


# --- restXml ser/de ---
def to_xml_text(value: InventoryOptionalField) -> str:
    return value


def from_xml_text(text: str) -> InventoryOptionalField:
    return cast(InventoryOptionalField, text)


def serialize_xml(value: InventoryOptionalField, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> InventoryOptionalField:
    return from_xml_text(el.text or "")
