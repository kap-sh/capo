"""Generated from Smithy shape ``com.amazonaws.ec2#SecureBlobAttributeValue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.secure_blob


class SecureBlobAttributeValue(TypedDict, closed=True):
    value: NotRequired["capo_ec2.types.secure_blob.SecureBlob"]
    """<p>The attribute value.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecureBlobAttributeValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "value" in value:
        import capo_ec2.types.secure_blob

        capo_ec2.types.secure_blob.serialize_ec2_query(
            value["value"], pairs, f"{key_prefix}Value"
        )


def deserialize_ec2_query(el: Element) -> SecureBlobAttributeValue:
    out: SecureBlobAttributeValue = {}  # type: ignore[typeddict-item]
    child_value = el.find("value")
    if child_value is not None:
        import capo_ec2.types.secure_blob

        out["value"] = capo_ec2.types.secure_blob.deserialize_ec2_query(child_value)
    return out


def redact_sensitive(value: SecureBlobAttributeValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
