"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationTypeDisplayHints``."""

from typing_extensions import NotRequired, TypedDict


class RegistrationTypeDisplayHints(TypedDict, closed=True):
    title: "str"
    """<p>The title of the display hint.</p>"""
    short_description: NotRequired["str"]
    """<p>A short description of the display hint.</p>"""
    long_description: NotRequired["str"]
    """<p>A full description of the display hint.</p>"""
    documentation_title: NotRequired["str"]
    """<p>The title of the document the display hint is associated with.</p>"""
    documentation_link: NotRequired["str"]
    """<p>The link to the document the display hint is associated with.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationTypeDisplayHints) -> dict:
    out: dict = {}
    out["Title"] = value["title"]
    if "short_description" in value:
        out["ShortDescription"] = value["short_description"]
    if "long_description" in value:
        out["LongDescription"] = value["long_description"]
    if "documentation_title" in value:
        out["DocumentationTitle"] = value["documentation_title"]
    if "documentation_link" in value:
        out["DocumentationLink"] = value["documentation_link"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RegistrationTypeDisplayHints:
    out: RegistrationTypeDisplayHints = {}  # type: ignore[typeddict-item]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        out["title"] = ""
    if data.get("ShortDescription") is not None:
        out["short_description"] = data["ShortDescription"]
    if data.get("LongDescription") is not None:
        out["long_description"] = data["LongDescription"]
    if data.get("DocumentationTitle") is not None:
        out["documentation_title"] = data["DocumentationTitle"]
    if data.get("DocumentationLink") is not None:
        out["documentation_link"] = data["DocumentationLink"]
    return out
