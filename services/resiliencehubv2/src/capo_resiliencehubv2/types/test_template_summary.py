"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestTemplateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.service_owned_arn


class TestTemplateSummary(TypedDict, closed=True):
    test_template_arn: "capo_resiliencehubv2.types.service_owned_arn.ServiceOwnedArn"
    """<p>The ARN of the test template.</p>"""
    name: "str"
    """<p>The name of the test template.</p>"""
    description: "str"
    """<p>A description of the test template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestTemplateSummary) -> dict:
    out: dict = {}
    out["testTemplateArn"] = value["test_template_arn"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> TestTemplateSummary:
    out: TestTemplateSummary = {}  # type: ignore[typeddict-item]
    if data.get("testTemplateArn") is not None:
        out["test_template_arn"] = data["testTemplateArn"]
    else:
        out["test_template_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    return out
