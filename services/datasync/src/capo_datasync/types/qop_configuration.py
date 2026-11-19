"""Generated from Smithy shape ``com.amazonaws.datasync#QopConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.hdfs_data_transfer_protection
    import capo_datasync.types.hdfs_rpc_protection


class QopConfiguration(TypedDict, closed=True):
    rpc_protection: NotRequired[
        "capo_datasync.types.hdfs_rpc_protection.HdfsRpcProtection"
    ]
    """<p>The RPC protection setting configured on the HDFS cluster. This setting corresponds to your <code>hadoop.rpc.protection</code> setting in your <code>core-site.xml</code> file on your Hadoop cluster.</p>"""
    data_transfer_protection: NotRequired[
        "capo_datasync.types.hdfs_data_transfer_protection.HdfsDataTransferProtection"
    ]
    """<p>The data transfer protection setting configured on the HDFS cluster. This setting corresponds to your <code>dfs.data.transfer.protection</code> setting in the <code>hdfs-site.xml</code> file on your Hadoop cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QopConfiguration) -> dict:
    out: dict = {}
    if "rpc_protection" in value:
        import capo_datasync.types.hdfs_rpc_protection

        out["RpcProtection"] = (
            capo_datasync.types.hdfs_rpc_protection.serialize_aws_json_1_1(
                value["rpc_protection"]
            )
        )
    if "data_transfer_protection" in value:
        import capo_datasync.types.hdfs_data_transfer_protection

        out["DataTransferProtection"] = (
            capo_datasync.types.hdfs_data_transfer_protection.serialize_aws_json_1_1(
                value["data_transfer_protection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QopConfiguration:
    out: QopConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("RpcProtection") is not None:
        import capo_datasync.types.hdfs_rpc_protection

        out["rpc_protection"] = (
            capo_datasync.types.hdfs_rpc_protection.deserialize_aws_json_1_1(
                data["RpcProtection"]
            )
        )
    if data.get("DataTransferProtection") is not None:
        import capo_datasync.types.hdfs_data_transfer_protection

        out["data_transfer_protection"] = (
            capo_datasync.types.hdfs_data_transfer_protection.deserialize_aws_json_1_1(
                data["DataTransferProtection"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: QopConfiguration) -> dict:
    out: dict = {}
    if "rpc_protection" in value:
        import capo_datasync.types.hdfs_rpc_protection

        out["RpcProtection"] = capo_datasync.types.hdfs_rpc_protection.serialize_cbor(
            value["rpc_protection"]
        )
    if "data_transfer_protection" in value:
        import capo_datasync.types.hdfs_data_transfer_protection

        out["DataTransferProtection"] = (
            capo_datasync.types.hdfs_data_transfer_protection.serialize_cbor(
                value["data_transfer_protection"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> QopConfiguration:
    out: QopConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("RpcProtection") is not None:
        import capo_datasync.types.hdfs_rpc_protection

        out["rpc_protection"] = (
            capo_datasync.types.hdfs_rpc_protection.deserialize_cbor(
                data["RpcProtection"]
            )
        )
    if data.get("DataTransferProtection") is not None:
        import capo_datasync.types.hdfs_data_transfer_protection

        out["data_transfer_protection"] = (
            capo_datasync.types.hdfs_data_transfer_protection.deserialize_cbor(
                data["DataTransferProtection"]
            )
        )
    return out
