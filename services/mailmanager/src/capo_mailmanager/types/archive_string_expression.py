"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveStringExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.archive_string_operator
    import capo_mailmanager.types.archive_string_to_evaluate
    import capo_mailmanager.types.string_value_list


class ArchiveStringExpression(TypedDict, closed=True):
    evaluate: (
        "capo_mailmanager.types.archive_string_to_evaluate.ArchiveStringToEvaluate"
    )
    """<p>The attribute of the email to evaluate.</p>"""
    operator: "capo_mailmanager.types.archive_string_operator.ArchiveStringOperator"
    """<p>The operator to use when evaluating the string values.</p>"""
    values: "capo_mailmanager.types.string_value_list.StringValueList"
    """<p>The list of string values to evaluate the email attribute against.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveStringExpression) -> dict:
    out: dict = {}
    import capo_mailmanager.types.archive_string_to_evaluate

    out["Evaluate"] = (
        capo_mailmanager.types.archive_string_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import capo_mailmanager.types.archive_string_operator

    out["Operator"] = (
        capo_mailmanager.types.archive_string_operator.serialize_aws_json_1_0(
            value["operator"]
        )
    )
    import capo_mailmanager.types.string_value_list

    out["Values"] = capo_mailmanager.types.string_value_list.serialize_aws_json_1_0(
        value["values"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ArchiveStringExpression:
    out: ArchiveStringExpression = {}  # type: ignore[typeddict-item]
    if data.get("Evaluate") is not None:
        import capo_mailmanager.types.archive_string_to_evaluate

        out["evaluate"] = (
            capo_mailmanager.types.archive_string_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        out["evaluate"] = {"$unknown": {"name": ""}}
    if data.get("Operator") is not None:
        import capo_mailmanager.types.archive_string_operator

        out["operator"] = (
            capo_mailmanager.types.archive_string_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_mailmanager.types.archive_string_operator.ArchiveStringOperator", ""
        )
    if data.get("Values") is not None:
        import capo_mailmanager.types.string_value_list

        out["values"] = (
            capo_mailmanager.types.string_value_list.deserialize_aws_json_1_0(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
