"""Generated from Smithy shape ``com.amazonaws.elementalinference#FunctionSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.context_type_list
    import capo_elementalinference.types.function_arn
    import capo_elementalinference.types.function_description
    import capo_elementalinference.types.function_id
    import capo_elementalinference.types.function_status
    import capo_elementalinference.types.function_target
    import capo_elementalinference.types.resource_name


class FunctionSummary(TypedDict, closed=True):
    arn: "capo_elementalinference.types.function_arn.FunctionArn"
    """<p>The ARN of the function.</p>"""
    id: "capo_elementalinference.types.function_id.FunctionId"
    """<p>The ID of the function.</p>"""
    name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>The name of the function.</p>"""
    description: NotRequired[
        "capo_elementalinference.types.function_description.FunctionDescription"
    ]
    """<p>The description of the function.</p>"""
    status: "capo_elementalinference.types.function_status.FunctionStatus"
    """<p>The status of the function.</p>"""
    target: NotRequired["capo_elementalinference.types.function_target.FunctionTarget"]
    """<p>The destination for the request that the function builds.</p>"""
    context_types: NotRequired[
        "capo_elementalinference.types.context_type_list.ContextTypeList"
    ]
    """<p>The kinds of media context that this function uses. Elemental Inference derives this field from the media paths that the request expression references; you can't set it. An empty list means that the expression references no media, so Elemental Inference supplies none at run time. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_elementalinference.types.function_status

    out["status"] = capo_elementalinference.types.function_status.serialize_json(
        value["status"]
    )
    if "target" in value:
        import capo_elementalinference.types.function_target

        out["target"] = capo_elementalinference.types.function_target.serialize_json(
            value["target"]
        )
    if "context_types" in value:
        import capo_elementalinference.types.context_type_list

        out["contextTypes"] = (
            capo_elementalinference.types.context_type_list.serialize_json(
                value["context_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> FunctionSummary:
    out: FunctionSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_elementalinference.types.function_status

        out["status"] = capo_elementalinference.types.function_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_elementalinference.types.function_status.FunctionStatus", ""
        )
    if data.get("target") is not None:
        import capo_elementalinference.types.function_target

        out["target"] = capo_elementalinference.types.function_target.deserialize_json(
            data["target"]
        )
    if data.get("contextTypes") is not None:
        import capo_elementalinference.types.context_type_list

        out["context_types"] = (
            capo_elementalinference.types.context_type_list.deserialize_json(
                data["contextTypes"]
            )
        )
    return out


def redact_sensitive(value: FunctionSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
