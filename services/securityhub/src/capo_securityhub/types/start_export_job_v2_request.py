"""Generated from Smithy shape ``com.amazonaws.securityhub#StartExportJobV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.client_token
    import capo_securityhub.types.export_destination
    import capo_securityhub.types.export_name
    import capo_securityhub.types.export_output
    import capo_securityhub.types.export_scopes


class StartExportJobV2Request(TypedDict, closed=True):
    name: NotRequired["capo_securityhub.types.export_name.ExportName"]
    """<p>An optional, user-provided name for the export job that helps you identify it in <code>ListExportJobsV2</code> results. The value can be 1–256 characters. Alphanumeric characters, spaces, and the following ASCII characters are permitted: <code>. _ , : ( ) / + -</code>.</p>"""
    destination: NotRequired[
        "capo_securityhub.types.export_destination.ExportDestination"
    ]
    """<p>The destination that Security Hub writes the export to. You must specify exactly one destination type. Currently, the only supported type is Amazon S3.</p>"""
    output_configuration: NotRequired[
        "capo_securityhub.types.export_output.ExportOutput"
    ]
    """<p>Specifies what data to export and how to format it. You must specify exactly one output type. Currently, the only supported type is <code>Findings</code>.</p>"""
    scopes: NotRequired["capo_securityhub.types.export_scopes.ExportScopes"]
    """<p>Limits the export to findings from specific organizational units (OUs) or from the delegated administrator's organization. Only the delegated administrator account can use this parameter; other accounts that specify it receive an <code>AccessDeniedException</code>.</p> <p>This parameter is optional. If you omit it, the delegated administrator exports findings from all accounts across the entire organization, and other accounts export only their own findings.</p> <p>You can specify up to 10 entries in <code>Scopes.AwsOrganizations</code>. If you specify multiple entries, Security Hub combines them using OR logic.</p>"""
    client_token: NotRequired["capo_securityhub.types.client_token.ClientToken"]
    """<p>A unique identifier used to ensure idempotency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartExportJobV2Request) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "destination" in value:
        import capo_securityhub.types.export_destination

        out["Destination"] = capo_securityhub.types.export_destination.serialize_json(
            value["destination"]
        )
    if "output_configuration" in value:
        import capo_securityhub.types.export_output

        out["OutputConfiguration"] = (
            capo_securityhub.types.export_output.serialize_json(
                value["output_configuration"]
            )
        )
    if "scopes" in value:
        import capo_securityhub.types.export_scopes

        out["Scopes"] = capo_securityhub.types.export_scopes.serialize_json(
            value["scopes"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartExportJobV2Request:
    out: StartExportJobV2Request = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Destination") is not None:
        import capo_securityhub.types.export_destination

        out["destination"] = capo_securityhub.types.export_destination.deserialize_json(
            data["Destination"]
        )
    if data.get("OutputConfiguration") is not None:
        import capo_securityhub.types.export_output

        out["output_configuration"] = (
            capo_securityhub.types.export_output.deserialize_json(
                data["OutputConfiguration"]
            )
        )
    if data.get("Scopes") is not None:
        import capo_securityhub.types.export_scopes

        out["scopes"] = capo_securityhub.types.export_scopes.deserialize_json(
            data["Scopes"]
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
