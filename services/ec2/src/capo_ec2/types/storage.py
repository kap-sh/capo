"""Generated from Smithy shape ``com.amazonaws.ec2#Storage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.s3_storage


class Storage(TypedDict, closed=True):
    s3: NotRequired["capo_ec2.types.s3_storage.S3Storage"]
    """<p>An Amazon S3 storage location.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Storage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "s3" in value:
        import capo_ec2.types.s3_storage

        capo_ec2.types.s3_storage.serialize_ec2_query(
            value["s3"], pairs, f"{key_prefix}S3"
        )


def deserialize_ec2_query(el: Element) -> Storage:
    out: Storage = {}  # type: ignore[typeddict-item]
    child_s3 = el.find("S3")
    if child_s3 is not None:
        import capo_ec2.types.s3_storage

        out["s3"] = capo_ec2.types.s3_storage.deserialize_ec2_query(child_s3)
    return out


def redact_sensitive(value: Storage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "s3" in value:
        import capo_ec2.types.s3_storage

        out["s3"] = capo_ec2.types.s3_storage.redact_sensitive(value["s3"])
    return out
