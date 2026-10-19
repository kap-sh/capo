"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionTypePermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.allowed_accounts


class ActionTypePermissions(TypedDict, closed=True):
    allowed_accounts: "capo_codepipeline.types.allowed_accounts.AllowedAccounts"
    """<p>A list of Amazon Web Services account IDs with access to use the action type in their pipelines.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionTypePermissions) -> dict:
    out: dict = {}
    import capo_codepipeline.types.allowed_accounts

    out["allowedAccounts"] = (
        capo_codepipeline.types.allowed_accounts.serialize_aws_json_1_1(
            value["allowed_accounts"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionTypePermissions:
    out: ActionTypePermissions = {}  # type: ignore[typeddict-item]
    if data.get("allowedAccounts") is not None:
        import capo_codepipeline.types.allowed_accounts

        out["allowed_accounts"] = (
            capo_codepipeline.types.allowed_accounts.deserialize_aws_json_1_1(
                data["allowedAccounts"]
            )
        )
    else:
        out["allowed_accounts"] = []
    return out
