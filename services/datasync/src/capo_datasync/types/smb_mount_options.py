"""Generated from Smithy shape ``com.amazonaws.datasync#SmbMountOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.smb_version


class SmbMountOptions(TypedDict, closed=True):
    version: NotRequired["capo_datasync.types.smb_version.SmbVersion"]
    """<p>By default, DataSync automatically chooses an SMB protocol version based on negotiation with your SMB file server. You also can configure DataSync to use a specific SMB version, but we recommend doing this only if DataSync has trouble negotiating with the SMB file server automatically.</p> <p>These are the following options for configuring the SMB version:</p> <ul> <li> <p> <code>AUTOMATIC</code> (default): DataSync and the SMB file server negotiate the highest version of SMB that they mutually support between 2.1 and 3.1.1.</p> <p>This is the recommended option. If you instead choose a specific version that your file server doesn't support, you may get an <code>Operation Not Supported</code> error.</p> </li> <li> <p> <code>SMB3</code>: Restricts the protocol negotiation to only SMB version 3.0.2.</p> </li> <li> <p> <code>SMB2</code>: Restricts the protocol negotiation to only SMB version 2.1.</p> </li> <li> <p> <code>SMB2_0</code>: Restricts the protocol negotiation to only SMB version 2.0.</p> </li> <li> <p> <code>SMB1</code>: Restricts the protocol negotiation to only SMB version 1.0.</p> <note> <p>The <code>SMB1</code> option isn't available when <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationFsxOntap.html">creating an Amazon FSx for NetApp ONTAP location</a>.</p> </note> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SmbMountOptions) -> dict:
    out: dict = {}
    if "version" in value:
        import capo_datasync.types.smb_version

        out["Version"] = capo_datasync.types.smb_version.serialize_aws_json_1_1(
            value["version"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SmbMountOptions:
    out: SmbMountOptions = {}  # type: ignore[typeddict-item]
    if data.get("Version") is not None:
        import capo_datasync.types.smb_version

        out["version"] = capo_datasync.types.smb_version.deserialize_aws_json_1_1(
            data["Version"]
        )
    return out
