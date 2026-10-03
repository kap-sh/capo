"""Generated from Smithy shape ``com.amazonaws.sns#CreatePlatformApplicationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sns.types.map_string_to_string
    import capo_sns.types.string


class CreatePlatformApplicationInput(TypedDict, closed=True):
    name: "capo_sns.types.string.String"
    """<p>Application names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, hyphens, and periods, and must be between 1 and 256 characters long.</p>"""
    platform: "capo_sns.types.string.String"
    """<p>The following platforms are supported: ADM (Amazon Device Messaging), APNS (Apple Push Notification Service), APNS_SANDBOX, and GCM (Firebase Cloud Messaging).</p>"""
    attributes: "capo_sns.types.map_string_to_string.MapStringToString"
    """<p>For a list of attributes, see <a href="https://docs.aws.amazon.com/sns/latest/api/API_SetPlatformApplicationAttributes.html"> <code>SetPlatformApplicationAttributes</code> </a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreatePlatformApplicationInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Name", str(value["name"])))
    pairs.append((f"{key_prefix}Platform", str(value["platform"])))
    import capo_sns.types.map_string_to_string

    capo_sns.types.map_string_to_string.serialize_query(
        value["attributes"], pairs, f"{key_prefix}Attributes"
    )


def deserialize_query(el: Element) -> CreatePlatformApplicationInput:
    out: CreatePlatformApplicationInput = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("CreatePlatformApplicationInput.name required")
    child_platform = el.find("Platform")
    if child_platform is not None:
        out["platform"] = str(child_platform.text or "")
    else:
        raise DeserializationError("CreatePlatformApplicationInput.platform required")
    child_attributes = el.find("Attributes")
    if child_attributes is not None:
        import capo_sns.types.map_string_to_string

        out["attributes"] = capo_sns.types.map_string_to_string.deserialize_query(
            child_attributes
        )
    else:
        raise DeserializationError("CreatePlatformApplicationInput.attributes required")
    return out
