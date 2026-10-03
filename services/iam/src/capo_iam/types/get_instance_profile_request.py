"""Generated from Smithy shape ``com.amazonaws.iam#GetInstanceProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.instance_profile_name_type


class GetInstanceProfileRequest(TypedDict, closed=True):
    instance_profile_name: (
        "capo_iam.types.instance_profile_name_type.instanceProfileNameType"
    )
    """<p>The name of the instance profile to get information about.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetInstanceProfileRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (f"{key_prefix}InstanceProfileName", str(value["instance_profile_name"]))
    )


def deserialize_query(el: Element) -> GetInstanceProfileRequest:
    out: GetInstanceProfileRequest = {}  # type: ignore[typeddict-item]
    child_instance_profile_name = el.find("InstanceProfileName")
    if child_instance_profile_name is not None:
        out["instance_profile_name"] = str(child_instance_profile_name.text or "")
    else:
        raise DeserializationError(
            "GetInstanceProfileRequest.instance_profile_name required"
        )
    return out
