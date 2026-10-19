"""Generated from Smithy shape ``com.amazonaws.acmpca#Qualifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.string256


class Qualifier(TypedDict, closed=True):
    cps_uri: "capo_acm_pca.types.string256.String256"
    """<p>Contains a pointer to a certification practice statement (CPS) published by the CA.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Qualifier) -> dict:
    out: dict = {}
    out["CpsUri"] = value["cps_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Qualifier:
    out: Qualifier = {}  # type: ignore[typeddict-item]
    if data.get("CpsUri") is not None:
        out["cps_uri"] = data["CpsUri"]
    else:
        out["cps_uri"] = ""
    return out
