"""Generated from Smithy shape ``com.amazonaws.directconnect#Interconnect``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.aws_device
    import capo_direct_connect.types.aws_device_v2
    import capo_direct_connect.types.aws_logical_device_id
    import capo_direct_connect.types.bandwidth
    import capo_direct_connect.types.encryption_mode
    import capo_direct_connect.types.has_logical_redundancy
    import capo_direct_connect.types.interconnect_id
    import capo_direct_connect.types.interconnect_name
    import capo_direct_connect.types.interconnect_state
    import capo_direct_connect.types.jumbo_frame_capable
    import capo_direct_connect.types.lag_id
    import capo_direct_connect.types.loa_issue_time
    import capo_direct_connect.types.location_code
    import capo_direct_connect.types.mac_sec_capable
    import capo_direct_connect.types.mac_sec_key_list
    import capo_direct_connect.types.port_encryption_status
    import capo_direct_connect.types.provider_name
    import capo_direct_connect.types.region
    import capo_direct_connect.types.tag_list


class Interconnect(TypedDict, closed=True):
    interconnect_id: NotRequired[
        "capo_direct_connect.types.interconnect_id.InterconnectId"
    ]
    """<p>The ID of the interconnect.</p>"""
    interconnect_name: NotRequired[
        "capo_direct_connect.types.interconnect_name.InterconnectName"
    ]
    """<p>The name of the interconnect.</p>"""
    interconnect_state: NotRequired[
        "capo_direct_connect.types.interconnect_state.InterconnectState"
    ]
    """<p>The state of the interconnect. The following are the possible values:</p> <ul> <li> <p> <code>requested</code>: The initial state of an interconnect. The interconnect stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.</p> </li> <li> <p> <code>pending</code>: The interconnect is approved, and is being initialized.</p> </li> <li> <p> <code>available</code>: The network link is up, and the interconnect is ready for use.</p> </li> <li> <p> <code>down</code>: The network link is down.</p> </li> <li> <p> <code>deleting</code>: The interconnect is being deleted.</p> </li> <li> <p> <code>deleted</code>: The interconnect is deleted.</p> </li> <li> <p> <code>unknown</code>: The state of the interconnect is not available.</p> </li> </ul>"""
    region: NotRequired["capo_direct_connect.types.region.Region"]
    """<p>The Amazon Web Services Region where the connection is located.</p>"""
    location: NotRequired["capo_direct_connect.types.location_code.LocationCode"]
    """<p>The location of the connection.</p>"""
    bandwidth: NotRequired["capo_direct_connect.types.bandwidth.Bandwidth"]
    """<p>The bandwidth of the connection.</p>"""
    loa_issue_time: NotRequired["capo_direct_connect.types.loa_issue_time.LoaIssueTime"]
    """<p>The time of the most recent call to <a>DescribeLoa</a> for this connection.</p>"""
    lag_id: NotRequired["capo_direct_connect.types.lag_id.LagId"]
    """<p>The ID of the LAG.</p>"""
    aws_device: NotRequired["capo_direct_connect.types.aws_device.AwsDevice"]
    """<p>The Direct Connect endpoint on which the physical connection terminates.</p>"""
    jumbo_frame_capable: NotRequired[
        "capo_direct_connect.types.jumbo_frame_capable.JumboFrameCapable"
    ]
    """<p>Indicates whether jumbo frames are supported.</p>"""
    aws_device_v2: NotRequired["capo_direct_connect.types.aws_device_v2.AwsDeviceV2"]
    """<p>The Direct Connect endpoint that terminates the physical connection.</p>"""
    aws_logical_device_id: NotRequired[
        "capo_direct_connect.types.aws_logical_device_id.AwsLogicalDeviceId"
    ]
    """<p>The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.</p>"""
    has_logical_redundancy: NotRequired[
        "capo_direct_connect.types.has_logical_redundancy.HasLogicalRedundancy"
    ]
    """<p>Indicates whether the interconnect supports a secondary BGP in the same address family (IPv4/IPv6).</p>"""
    tags: NotRequired["capo_direct_connect.types.tag_list.TagList"]
    """<p>The tags associated with the interconnect.</p>"""
    provider_name: NotRequired["capo_direct_connect.types.provider_name.ProviderName"]
    """<p>The name of the service provider associated with the interconnect.</p>"""
    mac_sec_capable: NotRequired[
        "capo_direct_connect.types.mac_sec_capable.MacSecCapable"
    ]
    """<p>Indicates whether the interconnect supports MAC Security (MACsec).</p>"""
    port_encryption_status: NotRequired[
        "capo_direct_connect.types.port_encryption_status.PortEncryptionStatus"
    ]
    """<p>The MAC Security (MACsec) port link status.</p> <p>The valid values are <code>Encryption Up</code>, which means that there is an active Connection Key Name, or <code>Encryption Down</code>.</p>"""
    encryption_mode: NotRequired[
        "capo_direct_connect.types.encryption_mode.EncryptionMode"
    ]
    """<p>The MAC Security (MACsec) encryption mode.</p> <p>The valid values are <code>no_encrypt</code>, <code>should_encrypt</code>, and <code>must_encrypt</code>.</p>"""
    mac_sec_keys: NotRequired[
        "capo_direct_connect.types.mac_sec_key_list.MacSecKeyList"
    ]
    """<p>The MAC Security (MACsec) security keys.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Interconnect) -> dict:
    out: dict = {}
    if "interconnect_id" in value:
        out["interconnectId"] = value["interconnect_id"]
    if "interconnect_name" in value:
        out["interconnectName"] = value["interconnect_name"]
    if "interconnect_state" in value:
        import capo_direct_connect.types.interconnect_state

        out["interconnectState"] = (
            capo_direct_connect.types.interconnect_state.serialize_aws_json_1_1(
                value["interconnect_state"]
            )
        )
    if "region" in value:
        out["region"] = value["region"]
    if "location" in value:
        out["location"] = value["location"]
    if "bandwidth" in value:
        out["bandwidth"] = value["bandwidth"]
    if "loa_issue_time" in value:
        import capo_direct_connect.types.loa_issue_time

        out["loaIssueTime"] = (
            capo_direct_connect.types.loa_issue_time.serialize_aws_json_1_1(
                value["loa_issue_time"]
            )
        )
    if "lag_id" in value:
        out["lagId"] = value["lag_id"]
    if "aws_device" in value:
        out["awsDevice"] = value["aws_device"]
    if "jumbo_frame_capable" in value:
        out["jumboFrameCapable"] = value["jumbo_frame_capable"]
    if "aws_device_v2" in value:
        out["awsDeviceV2"] = value["aws_device_v2"]
    if "aws_logical_device_id" in value:
        out["awsLogicalDeviceId"] = value["aws_logical_device_id"]
    if "has_logical_redundancy" in value:
        import capo_direct_connect.types.has_logical_redundancy

        out["hasLogicalRedundancy"] = (
            capo_direct_connect.types.has_logical_redundancy.serialize_aws_json_1_1(
                value["has_logical_redundancy"]
            )
        )
    if "tags" in value:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "provider_name" in value:
        out["providerName"] = value["provider_name"]
    if "mac_sec_capable" in value:
        out["macSecCapable"] = value["mac_sec_capable"]
    if "port_encryption_status" in value:
        out["portEncryptionStatus"] = value["port_encryption_status"]
    if "encryption_mode" in value:
        out["encryptionMode"] = value["encryption_mode"]
    if "mac_sec_keys" in value:
        import capo_direct_connect.types.mac_sec_key_list

        out["macSecKeys"] = (
            capo_direct_connect.types.mac_sec_key_list.serialize_aws_json_1_1(
                value["mac_sec_keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Interconnect:
    out: Interconnect = {}  # type: ignore[typeddict-item]
    if data.get("interconnectId") is not None:
        out["interconnect_id"] = data["interconnectId"]
    if data.get("interconnectName") is not None:
        out["interconnect_name"] = data["interconnectName"]
    if data.get("interconnectState") is not None:
        import capo_direct_connect.types.interconnect_state

        out["interconnect_state"] = (
            capo_direct_connect.types.interconnect_state.deserialize_aws_json_1_1(
                data["interconnectState"]
            )
        )
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("bandwidth") is not None:
        out["bandwidth"] = data["bandwidth"]
    if data.get("loaIssueTime") is not None:
        import capo_direct_connect.types.loa_issue_time

        out["loa_issue_time"] = (
            capo_direct_connect.types.loa_issue_time.deserialize_aws_json_1_1(
                data["loaIssueTime"]
            )
        )
    if data.get("lagId") is not None:
        out["lag_id"] = data["lagId"]
    if data.get("awsDevice") is not None:
        out["aws_device"] = data["awsDevice"]
    if data.get("jumboFrameCapable") is not None:
        out["jumbo_frame_capable"] = data["jumboFrameCapable"]
    if data.get("awsDeviceV2") is not None:
        out["aws_device_v2"] = data["awsDeviceV2"]
    if data.get("awsLogicalDeviceId") is not None:
        out["aws_logical_device_id"] = data["awsLogicalDeviceId"]
    if data.get("hasLogicalRedundancy") is not None:
        import capo_direct_connect.types.has_logical_redundancy

        out["has_logical_redundancy"] = (
            capo_direct_connect.types.has_logical_redundancy.deserialize_aws_json_1_1(
                data["hasLogicalRedundancy"]
            )
        )
    if data.get("tags") is not None:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("providerName") is not None:
        out["provider_name"] = data["providerName"]
    if data.get("macSecCapable") is not None:
        out["mac_sec_capable"] = data["macSecCapable"]
    if data.get("portEncryptionStatus") is not None:
        out["port_encryption_status"] = data["portEncryptionStatus"]
    if data.get("encryptionMode") is not None:
        out["encryption_mode"] = data["encryptionMode"]
    if data.get("macSecKeys") is not None:
        import capo_direct_connect.types.mac_sec_key_list

        out["mac_sec_keys"] = (
            capo_direct_connect.types.mac_sec_key_list.deserialize_aws_json_1_1(
                data["macSecKeys"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Interconnect) -> dict:
    out: dict = {}
    if "interconnect_id" in value:
        out["interconnectId"] = value["interconnect_id"]
    if "interconnect_name" in value:
        out["interconnectName"] = value["interconnect_name"]
    if "interconnect_state" in value:
        import capo_direct_connect.types.interconnect_state

        out["interconnectState"] = (
            capo_direct_connect.types.interconnect_state.serialize_cbor(
                value["interconnect_state"]
            )
        )
    if "region" in value:
        out["region"] = value["region"]
    if "location" in value:
        out["location"] = value["location"]
    if "bandwidth" in value:
        out["bandwidth"] = value["bandwidth"]
    if "loa_issue_time" in value:
        import capo_direct_connect.types.loa_issue_time

        out["loaIssueTime"] = capo_direct_connect.types.loa_issue_time.serialize_cbor(
            value["loa_issue_time"]
        )
    if "lag_id" in value:
        out["lagId"] = value["lag_id"]
    if "aws_device" in value:
        out["awsDevice"] = value["aws_device"]
    if "jumbo_frame_capable" in value:
        out["jumboFrameCapable"] = value["jumbo_frame_capable"]
    if "aws_device_v2" in value:
        out["awsDeviceV2"] = value["aws_device_v2"]
    if "aws_logical_device_id" in value:
        out["awsLogicalDeviceId"] = value["aws_logical_device_id"]
    if "has_logical_redundancy" in value:
        import capo_direct_connect.types.has_logical_redundancy

        out["hasLogicalRedundancy"] = (
            capo_direct_connect.types.has_logical_redundancy.serialize_cbor(
                value["has_logical_redundancy"]
            )
        )
    if "tags" in value:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.serialize_cbor(value["tags"])
    if "provider_name" in value:
        out["providerName"] = value["provider_name"]
    if "mac_sec_capable" in value:
        out["macSecCapable"] = value["mac_sec_capable"]
    if "port_encryption_status" in value:
        out["portEncryptionStatus"] = value["port_encryption_status"]
    if "encryption_mode" in value:
        out["encryptionMode"] = value["encryption_mode"]
    if "mac_sec_keys" in value:
        import capo_direct_connect.types.mac_sec_key_list

        out["macSecKeys"] = capo_direct_connect.types.mac_sec_key_list.serialize_cbor(
            value["mac_sec_keys"]
        )
    return out


def deserialize_cbor(data: dict) -> Interconnect:
    out: Interconnect = {}  # type: ignore[typeddict-item]
    if data.get("interconnectId") is not None:
        out["interconnect_id"] = data["interconnectId"]
    if data.get("interconnectName") is not None:
        out["interconnect_name"] = data["interconnectName"]
    if data.get("interconnectState") is not None:
        import capo_direct_connect.types.interconnect_state

        out["interconnect_state"] = (
            capo_direct_connect.types.interconnect_state.deserialize_cbor(
                data["interconnectState"]
            )
        )
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("bandwidth") is not None:
        out["bandwidth"] = data["bandwidth"]
    if data.get("loaIssueTime") is not None:
        import capo_direct_connect.types.loa_issue_time

        out["loa_issue_time"] = (
            capo_direct_connect.types.loa_issue_time.deserialize_cbor(
                data["loaIssueTime"]
            )
        )
    if data.get("lagId") is not None:
        out["lag_id"] = data["lagId"]
    if data.get("awsDevice") is not None:
        out["aws_device"] = data["awsDevice"]
    if data.get("jumboFrameCapable") is not None:
        out["jumbo_frame_capable"] = data["jumboFrameCapable"]
    if data.get("awsDeviceV2") is not None:
        out["aws_device_v2"] = data["awsDeviceV2"]
    if data.get("awsLogicalDeviceId") is not None:
        out["aws_logical_device_id"] = data["awsLogicalDeviceId"]
    if data.get("hasLogicalRedundancy") is not None:
        import capo_direct_connect.types.has_logical_redundancy

        out["has_logical_redundancy"] = (
            capo_direct_connect.types.has_logical_redundancy.deserialize_cbor(
                data["hasLogicalRedundancy"]
            )
        )
    if data.get("tags") is not None:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.deserialize_cbor(data["tags"])
    if data.get("providerName") is not None:
        out["provider_name"] = data["providerName"]
    if data.get("macSecCapable") is not None:
        out["mac_sec_capable"] = data["macSecCapable"]
    if data.get("portEncryptionStatus") is not None:
        out["port_encryption_status"] = data["portEncryptionStatus"]
    if data.get("encryptionMode") is not None:
        out["encryption_mode"] = data["encryptionMode"]
    if data.get("macSecKeys") is not None:
        import capo_direct_connect.types.mac_sec_key_list

        out["mac_sec_keys"] = (
            capo_direct_connect.types.mac_sec_key_list.deserialize_cbor(
                data["macSecKeys"]
            )
        )
    return out
