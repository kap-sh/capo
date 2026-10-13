"""Generated from Smithy shape ``com.amazonaws.iam#CreateAccessKeyResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.access_key


class CreateAccessKeyResponse(TypedDict, closed=True):
    access_key: "capo_iam.types.access_key.AccessKey"
    """<p>A structure with details about the access key.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateAccessKeyResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_iam.types.access_key

    capo_iam.types.access_key.serialize_query(
        value["access_key"], pairs, f"{key_prefix}AccessKey"
    )


def deserialize_query(el: Element) -> CreateAccessKeyResponse:
    out: CreateAccessKeyResponse = {}  # type: ignore[typeddict-item]
    child_access_key = el.find("AccessKey")
    if child_access_key is not None:
        import capo_iam.types.access_key

        out["access_key"] = capo_iam.types.access_key.deserialize_query(
            child_access_key
        )
    else:
        raise DeserializationError("CreateAccessKeyResponse.access_key required")
    return out


def redact_sensitive(value: CreateAccessKeyResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_key" in value:
        import capo_iam.types.access_key

        out["access_key"] = capo_iam.types.access_key.redact_sensitive(
            value["access_key"]
        )
    return out
