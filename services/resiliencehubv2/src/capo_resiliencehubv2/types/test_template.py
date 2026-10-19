"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.service_owned_arn
    import capo_resiliencehubv2.types.test_action_list
    import capo_resiliencehubv2.types.test_template_parameter_list


class TestTemplate(TypedDict, closed=True):
    test_template_arn: "capo_resiliencehubv2.types.service_owned_arn.ServiceOwnedArn"
    """<p>The ARN of the test template.</p>"""
    name: "str"
    """<p>The name of the test template.</p>"""
    description: NotRequired["str"]
    """<p>A description of the test template.</p>"""
    parameters: NotRequired[
        "capo_resiliencehubv2.types.test_template_parameter_list.TestTemplateParameterList"
    ]
    """<p>The parameters the test template accepts.</p>"""
    actions: NotRequired["capo_resiliencehubv2.types.test_action_list.TestActionList"]
    """<p>The fault actions the test template runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestTemplate) -> dict:
    out: dict = {}
    out["testTemplateArn"] = value["test_template_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "parameters" in value:
        import capo_resiliencehubv2.types.test_template_parameter_list

        out["parameters"] = (
            capo_resiliencehubv2.types.test_template_parameter_list.serialize_json(
                value["parameters"]
            )
        )
    if "actions" in value:
        import capo_resiliencehubv2.types.test_action_list

        out["actions"] = capo_resiliencehubv2.types.test_action_list.serialize_json(
            value["actions"]
        )
    return out


def deserialize_json(data: dict) -> TestTemplate:
    out: TestTemplate = {}  # type: ignore[typeddict-item]
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
    if data.get("parameters") is not None:
        import capo_resiliencehubv2.types.test_template_parameter_list

        out["parameters"] = (
            capo_resiliencehubv2.types.test_template_parameter_list.deserialize_json(
                data["parameters"]
            )
        )
    if data.get("actions") is not None:
        import capo_resiliencehubv2.types.test_action_list

        out["actions"] = capo_resiliencehubv2.types.test_action_list.deserialize_json(
            data["actions"]
        )
    return out
