"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateAddressListImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.address_list_id
    import capo_mailmanager.types.idempotency_token
    import capo_mailmanager.types.import_data_format
    import capo_mailmanager.types.job_name


class CreateAddressListImportJobRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_mailmanager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>"""
    address_list_id: "capo_mailmanager.types.address_list_id.AddressListId"
    """<p>The unique identifier of the address list for importing addresses to.</p>"""
    name: "capo_mailmanager.types.job_name.JobName"
    """<p>A user-friendly name for the import job.</p>"""
    import_data_format: "capo_mailmanager.types.import_data_format.ImportDataFormat"
    """<p>The format of the input for an import job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAddressListImportJobRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["AddressListId"] = value["address_list_id"]
    out["Name"] = value["name"]
    import capo_mailmanager.types.import_data_format

    out["ImportDataFormat"] = (
        capo_mailmanager.types.import_data_format.serialize_aws_json_1_0(
            value["import_data_format"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAddressListImportJobRequest:
    out: CreateAddressListImportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("AddressListId") is not None:
        out["address_list_id"] = data["AddressListId"]
    else:
        out["address_list_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ImportDataFormat") is not None:
        import capo_mailmanager.types.import_data_format

        out["import_data_format"] = (
            capo_mailmanager.types.import_data_format.deserialize_aws_json_1_0(
                data["ImportDataFormat"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAddressListImportJobRequest.import_data_format required"
        )
    return out
