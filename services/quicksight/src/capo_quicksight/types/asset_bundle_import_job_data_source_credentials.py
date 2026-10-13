"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSourceCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_data_source_credential_pair
    import capo_quicksight.types.secret_arn


class AssetBundleImportJobDataSourceCredentials(TypedDict, closed=True):
    credential_pair: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_data_source_credential_pair.AssetBundleImportJobDataSourceCredentialPair"
    ]
    """<p>A username and password credential pair to be used to create the imported data source. Keep this field blank if you are using a Secrets Manager secret to provide credentials.</p>"""
    secret_arn: NotRequired["capo_quicksight.types.secret_arn.SecretArn"]
    """<p>The ARN of the Secrets Manager secret that's used to create the imported data source. Keep this field blank, unless you are using a secret in place of a credential pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDataSourceCredentials) -> dict:
    out: dict = {}
    if "credential_pair" in value:
        import capo_quicksight.types.asset_bundle_import_job_data_source_credential_pair

        out["CredentialPair"] = (
            capo_quicksight.types.asset_bundle_import_job_data_source_credential_pair.serialize_json(
                value["credential_pair"]
            )
        )
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobDataSourceCredentials:
    out: AssetBundleImportJobDataSourceCredentials = {}  # type: ignore[typeddict-item]
    if data.get("CredentialPair") is not None:
        import capo_quicksight.types.asset_bundle_import_job_data_source_credential_pair

        out["credential_pair"] = (
            capo_quicksight.types.asset_bundle_import_job_data_source_credential_pair.deserialize_json(
                data["CredentialPair"]
            )
        )
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    return out


def redact_sensitive(
    value: AssetBundleImportJobDataSourceCredentials,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credential_pair" in value:
        out["credential_pair"] = "*** Sensitive Data Redacted ***"
    return out
