"""Generated from Smithy shape ``com.amazonaws.directconnect#RouterType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.platform
    import capo_direct_connect.types.router_type_identifier
    import capo_direct_connect.types.software
    import capo_direct_connect.types.vendor
    import capo_direct_connect.types.xslt_template_name
    import capo_direct_connect.types.xslt_template_name_for_mac_sec


class RouterType(TypedDict, closed=True):
    vendor: NotRequired["capo_direct_connect.types.vendor.Vendor"]
    """<p>The vendor for the virtual interface's router.</p>"""
    platform: NotRequired["capo_direct_connect.types.platform.Platform"]
    """<p>The virtual interface router platform.</p>"""
    software: NotRequired["capo_direct_connect.types.software.Software"]
    """<p>The router software. </p>"""
    xslt_template_name: NotRequired[
        "capo_direct_connect.types.xslt_template_name.XsltTemplateName"
    ]
    """<p>The template for the virtual interface's router.</p>"""
    xslt_template_name_for_mac_sec: NotRequired[
        "capo_direct_connect.types.xslt_template_name_for_mac_sec.XsltTemplateNameForMacSec"
    ]
    """<p>The MAC Security (MACsec) template for the virtual interface's router.</p>"""
    router_type_identifier: NotRequired[
        "capo_direct_connect.types.router_type_identifier.RouterTypeIdentifier"
    ]
    """<p>Identifies the router by a combination of vendor, platform, and software version. For example, <code>CiscoSystemsInc-2900SeriesRouters-IOS124</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RouterType) -> dict:
    out: dict = {}
    if "vendor" in value:
        out["vendor"] = value["vendor"]
    if "platform" in value:
        out["platform"] = value["platform"]
    if "software" in value:
        out["software"] = value["software"]
    if "xslt_template_name" in value:
        out["xsltTemplateName"] = value["xslt_template_name"]
    if "xslt_template_name_for_mac_sec" in value:
        out["xsltTemplateNameForMacSec"] = value["xslt_template_name_for_mac_sec"]
    if "router_type_identifier" in value:
        out["routerTypeIdentifier"] = value["router_type_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RouterType:
    out: RouterType = {}  # type: ignore[typeddict-item]
    if data.get("vendor") is not None:
        out["vendor"] = data["vendor"]
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    if data.get("software") is not None:
        out["software"] = data["software"]
    if data.get("xsltTemplateName") is not None:
        out["xslt_template_name"] = data["xsltTemplateName"]
    if data.get("xsltTemplateNameForMacSec") is not None:
        out["xslt_template_name_for_mac_sec"] = data["xsltTemplateNameForMacSec"]
    if data.get("routerTypeIdentifier") is not None:
        out["router_type_identifier"] = data["routerTypeIdentifier"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RouterType) -> dict:
    out: dict = {}
    if "vendor" in value:
        out["vendor"] = value["vendor"]
    if "platform" in value:
        out["platform"] = value["platform"]
    if "software" in value:
        out["software"] = value["software"]
    if "xslt_template_name" in value:
        out["xsltTemplateName"] = value["xslt_template_name"]
    if "xslt_template_name_for_mac_sec" in value:
        out["xsltTemplateNameForMacSec"] = value["xslt_template_name_for_mac_sec"]
    if "router_type_identifier" in value:
        out["routerTypeIdentifier"] = value["router_type_identifier"]
    return out


def deserialize_cbor(data: dict) -> RouterType:
    out: RouterType = {}  # type: ignore[typeddict-item]
    if data.get("vendor") is not None:
        out["vendor"] = data["vendor"]
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    if data.get("software") is not None:
        out["software"] = data["software"]
    if data.get("xsltTemplateName") is not None:
        out["xslt_template_name"] = data["xsltTemplateName"]
    if data.get("xsltTemplateNameForMacSec") is not None:
        out["xslt_template_name_for_mac_sec"] = data["xsltTemplateNameForMacSec"]
    if data.get("routerTypeIdentifier") is not None:
        out["router_type_identifier"] = data["routerTypeIdentifier"]
    return out
