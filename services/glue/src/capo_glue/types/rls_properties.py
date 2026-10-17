"""Generated from Smithy shape ``com.amazonaws.glue#RLSProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.name_string


class RLSProperties(TypedDict, closed=True):
    default_rls_policy: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the default row-level security policy applied to the table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RLSProperties) -> dict:
    out: dict = {}
    if "default_rls_policy" in value:
        out["DefaultRLSPolicy"] = value["default_rls_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RLSProperties:
    out: RLSProperties = {}  # type: ignore[typeddict-item]
    if data.get("DefaultRLSPolicy") is not None:
        out["default_rls_policy"] = data["DefaultRLSPolicy"]
    return out
