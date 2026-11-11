"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetTemporaryGlueFunctionCredentialsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.audit_context
    import capo_lakeformation.types.resource_arn_string


class GetTemporaryGlueFunctionCredentialsRequest(TypedDict, closed=True):
    user_defined_function_arn: (
        "capo_lakeformation.types.resource_arn_string.ResourceArnString"
    )
    """<p>The ARN of the user-defined function whose artifacts you want to download, in the format <code>arn:aws:glue:<i>region</i>:<i>account-id</i>:userDefinedFunction/<i>database-name</i>/<i>function-name</i> </code>.</p>"""
    audit_context: NotRequired["capo_lakeformation.types.audit_context.AuditContext"]
    """<p>Context for the request, such as the column names and query ID, that Lake Formation uses for auditing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTemporaryGlueFunctionCredentialsRequest) -> dict:
    out: dict = {}
    out["UserDefinedFunctionArn"] = value["user_defined_function_arn"]
    if "audit_context" in value:
        import capo_lakeformation.types.audit_context

        out["AuditContext"] = capo_lakeformation.types.audit_context.serialize_json(
            value["audit_context"]
        )
    return out


def deserialize_json(data: dict) -> GetTemporaryGlueFunctionCredentialsRequest:
    out: GetTemporaryGlueFunctionCredentialsRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserDefinedFunctionArn") is not None:
        out["user_defined_function_arn"] = data["UserDefinedFunctionArn"]
    else:
        out["user_defined_function_arn"] = ""
    if data.get("AuditContext") is not None:
        import capo_lakeformation.types.audit_context

        out["audit_context"] = capo_lakeformation.types.audit_context.deserialize_json(
            data["AuditContext"]
        )
    return out
