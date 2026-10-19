"""Generated from Smithy shape ``com.amazonaws.fis#CreateTargetAccountConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.client_token
    import capo_fis.types.experiment_template_id
    import capo_fis.types.role_arn
    import capo_fis.types.target_account_configuration_description
    import capo_fis.types.target_account_id


class CreateTargetAccountConfigurationRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_fis.types.client_token.ClientToken"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    experiment_template_id: "capo_fis.types.experiment_template_id.ExperimentTemplateId"
    """<p>The experiment template ID.</p>"""
    account_id: "capo_fis.types.target_account_id.TargetAccountId"
    """<p>The Amazon Web Services account ID of the target account.</p>"""
    role_arn: "capo_fis.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role for the target account.</p>"""
    description: NotRequired[
        "capo_fis.types.target_account_configuration_description.TargetAccountConfigurationDescription"
    ]
    """<p>The description of the target account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTargetAccountConfigurationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["roleArn"] = value["role_arn"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateTargetAccountConfigurationRequest:
    out: CreateTargetAccountConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
