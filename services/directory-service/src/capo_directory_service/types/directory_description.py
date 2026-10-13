"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryDescription``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.access_url
    import capo_directory_service.types.alias_name
    import capo_directory_service.types.description
    import capo_directory_service.types.desired_number_of_domain_controllers
    import capo_directory_service.types.directory_connect_settings_description
    import capo_directory_service.types.directory_edition
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.directory_name
    import capo_directory_service.types.directory_short_name
    import capo_directory_service.types.directory_size
    import capo_directory_service.types.directory_stage
    import capo_directory_service.types.directory_type
    import capo_directory_service.types.directory_vpc_settings_description
    import capo_directory_service.types.dns_ip_addrs
    import capo_directory_service.types.dns_ipv6_addrs
    import capo_directory_service.types.hybrid_settings_description
    import capo_directory_service.types.last_updated_date_time
    import capo_directory_service.types.launch_time
    import capo_directory_service.types.network_type
    import capo_directory_service.types.notes
    import capo_directory_service.types.os_version
    import capo_directory_service.types.owner_directory_description
    import capo_directory_service.types.radius_settings
    import capo_directory_service.types.radius_status
    import capo_directory_service.types.regions_info
    import capo_directory_service.types.share_method
    import capo_directory_service.types.share_status
    import capo_directory_service.types.sso_enabled
    import capo_directory_service.types.stage_reason


class DirectoryDescription(TypedDict, closed=True):
    directory_id: NotRequired["capo_directory_service.types.directory_id.DirectoryId"]
    """<p>The directory identifier.</p>"""
    name: NotRequired["capo_directory_service.types.directory_name.DirectoryName"]
    """<p>The fully qualified name of the directory.</p>"""
    short_name: NotRequired[
        "capo_directory_service.types.directory_short_name.DirectoryShortName"
    ]
    """<p>The short name of the directory.</p>"""
    size: NotRequired["capo_directory_service.types.directory_size.DirectorySize"]
    """<p>The directory size.</p>"""
    edition: NotRequired[
        "capo_directory_service.types.directory_edition.DirectoryEdition"
    ]
    """<p>The edition associated with this directory.</p>"""
    alias: NotRequired["capo_directory_service.types.alias_name.AliasName"]
    """<p>The alias for the directory. If no alias exists, the alias is the directory identifier, such as <code>d-XXXXXXXXXX</code>.</p>"""
    access_url: NotRequired["capo_directory_service.types.access_url.AccessUrl"]
    """<p>The access URL for the directory, such as <code>http://<alias>.awsapps.com</code>. If no alias exists, <code><alias></code> is the directory identifier, such as <code>d-XXXXXXXXXX</code>.</p>"""
    description: NotRequired["capo_directory_service.types.description.Description"]
    """<p>The description for the directory.</p>"""
    dns_ip_addrs: NotRequired["capo_directory_service.types.dns_ip_addrs.DnsIpAddrs"]
    """<p>The IP addresses of the DNS servers for the directory. For a Simple AD or Microsoft AD directory, these are the IP addresses of the Simple AD or Microsoft AD directory servers. For an AD Connector directory, these are the IP addresses of self-managed directory to which the AD Connector is connected.</p>"""
    dns_ipv6_addrs: NotRequired[
        "capo_directory_service.types.dns_ipv6_addrs.DnsIpv6Addrs"
    ]
    """<p>The IPv6 addresses of the DNS servers for the directory. For a Simple AD or Microsoft AD directory, these are the IPv6 addresses of the Simple AD or Microsoft AD directory servers. For an AD Connector directory, these are the IPv6 addresses of the DNS servers or domain controllers in your self-managed directory to which the AD Connector is connected.</p>"""
    stage: NotRequired["capo_directory_service.types.directory_stage.DirectoryStage"]
    """<p>The current stage of the directory.</p>"""
    share_status: NotRequired["capo_directory_service.types.share_status.ShareStatus"]
    """<p>Current directory status of the shared Managed Microsoft AD directory.</p>"""
    share_method: NotRequired["capo_directory_service.types.share_method.ShareMethod"]
    """<p>The method used when sharing a directory to determine whether the directory should be shared within your Amazon Web Services organization (<code>ORGANIZATIONS</code>) or with any Amazon Web Services account by sending a shared directory request (<code>HANDSHAKE</code>).</p>"""
    share_notes: NotRequired["capo_directory_service.types.notes.Notes"]
    """<p>A directory share request that is sent by the directory owner to the directory consumer. The request includes a typed message to help the directory consumer administrator determine whether to approve or reject the share invitation.</p>"""
    launch_time: NotRequired["capo_directory_service.types.launch_time.LaunchTime"]
    """<p>The date and time when the directory was created.</p>"""
    stage_last_updated_date_time: NotRequired[
        "capo_directory_service.types.last_updated_date_time.LastUpdatedDateTime"
    ]
    """<p>The date and time when the stage was last updated.</p>"""
    type: NotRequired["capo_directory_service.types.directory_type.DirectoryType"]
    """<p>The directory type.</p>"""
    vpc_settings: NotRequired[
        "capo_directory_service.types.directory_vpc_settings_description.DirectoryVpcSettingsDescription"
    ]
    """<p>A <a>DirectoryVpcSettingsDescription</a> object that contains additional information about a directory. Present only for Simple AD and Managed Microsoft AD directories.</p>"""
    connect_settings: NotRequired[
        "capo_directory_service.types.directory_connect_settings_description.DirectoryConnectSettingsDescription"
    ]
    """<p> <a>DirectoryConnectSettingsDescription</a> object that contains additional information about an AD Connector directory. Present only for AD Connector directories.</p>"""
    radius_settings: NotRequired[
        "capo_directory_service.types.radius_settings.RadiusSettings"
    ]
    """<p>Information about the <a>RadiusSettings</a> object configured for this directory.</p>"""
    radius_status: NotRequired[
        "capo_directory_service.types.radius_status.RadiusStatus"
    ]
    """<p>The status of the RADIUS MFA server connection.</p>"""
    stage_reason: NotRequired["capo_directory_service.types.stage_reason.StageReason"]
    """<p>Additional information about the directory stage.</p>"""
    sso_enabled: "capo_directory_service.types.sso_enabled.SsoEnabled"
    """<p>Indicates whether single sign-on is enabled for the directory. For more information, see <a>EnableSso</a> and <a>DisableSso</a>.</p>"""
    desired_number_of_domain_controllers: NotRequired[
        "capo_directory_service.types.desired_number_of_domain_controllers.DesiredNumberOfDomainControllers"
    ]
    """<p>The desired number of domain controllers in the directory if the directory is Microsoft AD.</p>"""
    owner_directory_description: NotRequired[
        "capo_directory_service.types.owner_directory_description.OwnerDirectoryDescription"
    ]
    """<p>Describes the Managed Microsoft AD directory in the directory owner account.</p>"""
    regions_info: NotRequired["capo_directory_service.types.regions_info.RegionsInfo"]
    """<p>Lists the Regions where the directory has replicated.</p>"""
    os_version: NotRequired["capo_directory_service.types.os_version.OSVersion"]
    """<p>The operating system (OS) version of the directory.</p>"""
    hybrid_settings: NotRequired[
        "capo_directory_service.types.hybrid_settings_description.HybridSettingsDescription"
    ]
    """<p>Contains information about the hybrid directory configuration for the directory, including Amazon Web Services System Manager managed node identifiers and DNS IPs.</p>"""
    network_type: NotRequired["capo_directory_service.types.network_type.NetworkType"]
    """<p>The network type of the directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryDescription) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "short_name" in value:
        out["ShortName"] = value["short_name"]
    if "size" in value:
        import capo_directory_service.types.directory_size

        out["Size"] = (
            capo_directory_service.types.directory_size.serialize_aws_json_1_1(
                value["size"]
            )
        )
    if "edition" in value:
        import capo_directory_service.types.directory_edition

        out["Edition"] = (
            capo_directory_service.types.directory_edition.serialize_aws_json_1_1(
                value["edition"]
            )
        )
    if "alias" in value:
        out["Alias"] = value["alias"]
    if "access_url" in value:
        out["AccessUrl"] = value["access_url"]
    if "description" in value:
        out["Description"] = value["description"]
    if "dns_ip_addrs" in value:
        import capo_directory_service.types.dns_ip_addrs

        out["DnsIpAddrs"] = (
            capo_directory_service.types.dns_ip_addrs.serialize_aws_json_1_1(
                value["dns_ip_addrs"]
            )
        )
    if "dns_ipv6_addrs" in value:
        import capo_directory_service.types.dns_ipv6_addrs

        out["DnsIpv6Addrs"] = (
            capo_directory_service.types.dns_ipv6_addrs.serialize_aws_json_1_1(
                value["dns_ipv6_addrs"]
            )
        )
    if "stage" in value:
        import capo_directory_service.types.directory_stage

        out["Stage"] = (
            capo_directory_service.types.directory_stage.serialize_aws_json_1_1(
                value["stage"]
            )
        )
    if "share_status" in value:
        import capo_directory_service.types.share_status

        out["ShareStatus"] = (
            capo_directory_service.types.share_status.serialize_aws_json_1_1(
                value["share_status"]
            )
        )
    if "share_method" in value:
        import capo_directory_service.types.share_method

        out["ShareMethod"] = (
            capo_directory_service.types.share_method.serialize_aws_json_1_1(
                value["share_method"]
            )
        )
    if "share_notes" in value:
        out["ShareNotes"] = value["share_notes"]
    if "launch_time" in value:
        import capo_directory_service.types.launch_time

        out["LaunchTime"] = (
            capo_directory_service.types.launch_time.serialize_aws_json_1_1(
                value["launch_time"]
            )
        )
    if "stage_last_updated_date_time" in value:
        import capo_directory_service.types.last_updated_date_time

        out["StageLastUpdatedDateTime"] = (
            capo_directory_service.types.last_updated_date_time.serialize_aws_json_1_1(
                value["stage_last_updated_date_time"]
            )
        )
    if "type" in value:
        import capo_directory_service.types.directory_type

        out["Type"] = (
            capo_directory_service.types.directory_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "vpc_settings" in value:
        import capo_directory_service.types.directory_vpc_settings_description

        out["VpcSettings"] = (
            capo_directory_service.types.directory_vpc_settings_description.serialize_aws_json_1_1(
                value["vpc_settings"]
            )
        )
    if "connect_settings" in value:
        import capo_directory_service.types.directory_connect_settings_description

        out["ConnectSettings"] = (
            capo_directory_service.types.directory_connect_settings_description.serialize_aws_json_1_1(
                value["connect_settings"]
            )
        )
    if "radius_settings" in value:
        import capo_directory_service.types.radius_settings

        out["RadiusSettings"] = (
            capo_directory_service.types.radius_settings.serialize_aws_json_1_1(
                value["radius_settings"]
            )
        )
    if "radius_status" in value:
        import capo_directory_service.types.radius_status

        out["RadiusStatus"] = (
            capo_directory_service.types.radius_status.serialize_aws_json_1_1(
                value["radius_status"]
            )
        )
    if "stage_reason" in value:
        out["StageReason"] = value["stage_reason"]
    out["SsoEnabled"] = value.get("sso_enabled", False)
    if "desired_number_of_domain_controllers" in value:
        out["DesiredNumberOfDomainControllers"] = value[
            "desired_number_of_domain_controllers"
        ]
    if "owner_directory_description" in value:
        import capo_directory_service.types.owner_directory_description

        out["OwnerDirectoryDescription"] = (
            capo_directory_service.types.owner_directory_description.serialize_aws_json_1_1(
                value["owner_directory_description"]
            )
        )
    if "regions_info" in value:
        import capo_directory_service.types.regions_info

        out["RegionsInfo"] = (
            capo_directory_service.types.regions_info.serialize_aws_json_1_1(
                value["regions_info"]
            )
        )
    if "os_version" in value:
        import capo_directory_service.types.os_version

        out["OsVersion"] = (
            capo_directory_service.types.os_version.serialize_aws_json_1_1(
                value["os_version"]
            )
        )
    if "hybrid_settings" in value:
        import capo_directory_service.types.hybrid_settings_description

        out["HybridSettings"] = (
            capo_directory_service.types.hybrid_settings_description.serialize_aws_json_1_1(
                value["hybrid_settings"]
            )
        )
    if "network_type" in value:
        import capo_directory_service.types.network_type

        out["NetworkType"] = (
            capo_directory_service.types.network_type.serialize_aws_json_1_1(
                value["network_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectoryDescription:
    out: DirectoryDescription = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ShortName") is not None:
        out["short_name"] = data["ShortName"]
    if data.get("Size") is not None:
        import capo_directory_service.types.directory_size

        out["size"] = (
            capo_directory_service.types.directory_size.deserialize_aws_json_1_1(
                data["Size"]
            )
        )
    if data.get("Edition") is not None:
        import capo_directory_service.types.directory_edition

        out["edition"] = (
            capo_directory_service.types.directory_edition.deserialize_aws_json_1_1(
                data["Edition"]
            )
        )
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    if data.get("AccessUrl") is not None:
        out["access_url"] = data["AccessUrl"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DnsIpAddrs") is not None:
        import capo_directory_service.types.dns_ip_addrs

        out["dns_ip_addrs"] = (
            capo_directory_service.types.dns_ip_addrs.deserialize_aws_json_1_1(
                data["DnsIpAddrs"]
            )
        )
    if data.get("DnsIpv6Addrs") is not None:
        import capo_directory_service.types.dns_ipv6_addrs

        out["dns_ipv6_addrs"] = (
            capo_directory_service.types.dns_ipv6_addrs.deserialize_aws_json_1_1(
                data["DnsIpv6Addrs"]
            )
        )
    if data.get("Stage") is not None:
        import capo_directory_service.types.directory_stage

        out["stage"] = (
            capo_directory_service.types.directory_stage.deserialize_aws_json_1_1(
                data["Stage"]
            )
        )
    if data.get("ShareStatus") is not None:
        import capo_directory_service.types.share_status

        out["share_status"] = (
            capo_directory_service.types.share_status.deserialize_aws_json_1_1(
                data["ShareStatus"]
            )
        )
    if data.get("ShareMethod") is not None:
        import capo_directory_service.types.share_method

        out["share_method"] = (
            capo_directory_service.types.share_method.deserialize_aws_json_1_1(
                data["ShareMethod"]
            )
        )
    if data.get("ShareNotes") is not None:
        out["share_notes"] = data["ShareNotes"]
    if data.get("LaunchTime") is not None:
        import capo_directory_service.types.launch_time

        out["launch_time"] = (
            capo_directory_service.types.launch_time.deserialize_aws_json_1_1(
                data["LaunchTime"]
            )
        )
    if data.get("StageLastUpdatedDateTime") is not None:
        import capo_directory_service.types.last_updated_date_time

        out["stage_last_updated_date_time"] = (
            capo_directory_service.types.last_updated_date_time.deserialize_aws_json_1_1(
                data["StageLastUpdatedDateTime"]
            )
        )
    if data.get("Type") is not None:
        import capo_directory_service.types.directory_type

        out["type"] = (
            capo_directory_service.types.directory_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("VpcSettings") is not None:
        import capo_directory_service.types.directory_vpc_settings_description

        out["vpc_settings"] = (
            capo_directory_service.types.directory_vpc_settings_description.deserialize_aws_json_1_1(
                data["VpcSettings"]
            )
        )
    if data.get("ConnectSettings") is not None:
        import capo_directory_service.types.directory_connect_settings_description

        out["connect_settings"] = (
            capo_directory_service.types.directory_connect_settings_description.deserialize_aws_json_1_1(
                data["ConnectSettings"]
            )
        )
    if data.get("RadiusSettings") is not None:
        import capo_directory_service.types.radius_settings

        out["radius_settings"] = (
            capo_directory_service.types.radius_settings.deserialize_aws_json_1_1(
                data["RadiusSettings"]
            )
        )
    if data.get("RadiusStatus") is not None:
        import capo_directory_service.types.radius_status

        out["radius_status"] = (
            capo_directory_service.types.radius_status.deserialize_aws_json_1_1(
                data["RadiusStatus"]
            )
        )
    if data.get("StageReason") is not None:
        out["stage_reason"] = data["StageReason"]
    if data.get("SsoEnabled") is not None:
        out["sso_enabled"] = data["SsoEnabled"]
    else:
        out["sso_enabled"] = False
    if data.get("DesiredNumberOfDomainControllers") is not None:
        out["desired_number_of_domain_controllers"] = data[
            "DesiredNumberOfDomainControllers"
        ]
    if data.get("OwnerDirectoryDescription") is not None:
        import capo_directory_service.types.owner_directory_description

        out["owner_directory_description"] = (
            capo_directory_service.types.owner_directory_description.deserialize_aws_json_1_1(
                data["OwnerDirectoryDescription"]
            )
        )
    if data.get("RegionsInfo") is not None:
        import capo_directory_service.types.regions_info

        out["regions_info"] = (
            capo_directory_service.types.regions_info.deserialize_aws_json_1_1(
                data["RegionsInfo"]
            )
        )
    if data.get("OsVersion") is not None:
        import capo_directory_service.types.os_version

        out["os_version"] = (
            capo_directory_service.types.os_version.deserialize_aws_json_1_1(
                data["OsVersion"]
            )
        )
    if data.get("HybridSettings") is not None:
        import capo_directory_service.types.hybrid_settings_description

        out["hybrid_settings"] = (
            capo_directory_service.types.hybrid_settings_description.deserialize_aws_json_1_1(
                data["HybridSettings"]
            )
        )
    if data.get("NetworkType") is not None:
        import capo_directory_service.types.network_type

        out["network_type"] = (
            capo_directory_service.types.network_type.deserialize_aws_json_1_1(
                data["NetworkType"]
            )
        )
    return out


def redact_sensitive(value: DirectoryDescription) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "share_notes" in value:
        out["share_notes"] = "*** Sensitive Data Redacted ***"
    if "radius_settings" in value:
        import capo_directory_service.types.radius_settings

        out["radius_settings"] = (
            capo_directory_service.types.radius_settings.redact_sensitive(
                value["radius_settings"]
            )
        )
    if "owner_directory_description" in value:
        import capo_directory_service.types.owner_directory_description

        out["owner_directory_description"] = (
            capo_directory_service.types.owner_directory_description.redact_sensitive(
                value["owner_directory_description"]
            )
        )
    return out
