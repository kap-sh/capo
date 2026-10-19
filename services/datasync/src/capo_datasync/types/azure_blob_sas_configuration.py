"""Generated from Smithy shape ``com.amazonaws.datasync#AzureBlobSasConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.azure_blob_sas_token


class AzureBlobSasConfiguration(TypedDict, closed=True):
    token: "capo_datasync.types.azure_blob_sas_token.AzureBlobSasToken"
    """<p>Specifies a SAS token that provides permissions to access your Azure Blob Storage.</p> <p>The token is part of the SAS URI string that comes after the storage resource URI and a question mark. A token looks something like this:</p> <p> <code>sp=r&st=2023-12-20T14:54:52Z&se=2023-12-20T22:54:52Z&spr=https&sv=2021-06-08&sr=c&sig=aBBKDWQvyuVcTPH9EBp%2FXTI9E%2F%2Fmq171%2BZU178wcwqU%3D</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AzureBlobSasConfiguration) -> dict:
    out: dict = {}
    out["Token"] = value["token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AzureBlobSasConfiguration:
    out: AzureBlobSasConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Token") is not None:
        out["token"] = data["Token"]
    else:
        out["token"] = ""
    return out


def redact_sensitive(value: AzureBlobSasConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "token" in value:
        out["token"] = "*** Sensitive Data Redacted ***"
    return out
