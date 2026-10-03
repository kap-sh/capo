"""Generated from Smithy shape ``com.amazonaws.ec2#EbsInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.attachment_limit_type
    import capo_ec2.types.ebs_card_info_list
    import capo_ec2.types.ebs_encryption_support
    import capo_ec2.types.ebs_nvme_support
    import capo_ec2.types.ebs_optimized_info
    import capo_ec2.types.ebs_optimized_support
    import capo_ec2.types.maximum_ebs_attachments
    import capo_ec2.types.maximum_ebs_cards


class EbsInfo(TypedDict, closed=True):
    ebs_optimized_support: NotRequired[
        "capo_ec2.types.ebs_optimized_support.EbsOptimizedSupport"
    ]
    """<p>Indicates whether the instance type is Amazon EBS-optimized. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html">Amazon EBS-optimized instances</a> in <i>Amazon EC2 User Guide</i>.</p>"""
    encryption_support: NotRequired[
        "capo_ec2.types.ebs_encryption_support.EbsEncryptionSupport"
    ]
    """<p>Indicates whether Amazon EBS encryption is supported.</p>"""
    ebs_optimized_info: NotRequired[
        "capo_ec2.types.ebs_optimized_info.EbsOptimizedInfo"
    ]
    """<p>Describes the optimized EBS performance for the instance type.</p>"""
    nvme_support: NotRequired["capo_ec2.types.ebs_nvme_support.EbsNvmeSupport"]
    """<p>Indicates whether non-volatile memory express (NVMe) is supported.</p>"""
    maximum_ebs_attachments: NotRequired[
        "capo_ec2.types.maximum_ebs_attachments.MaximumEbsAttachments"
    ]
    """<p>Indicates the maximum number of Amazon EBS volumes that can be attached to the instance type. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html">Amazon EBS volume limits for Amazon EC2 instances</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    attachment_limit_type: NotRequired[
        "capo_ec2.types.attachment_limit_type.AttachmentLimitType"
    ]
    """<p>Indicates whether the instance type features a shared or dedicated Amazon EBS volume attachment limit. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html">Amazon EBS volume limits for Amazon EC2 instances</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    maximum_ebs_cards: NotRequired["capo_ec2.types.maximum_ebs_cards.MaximumEbsCards"]
    """<p>Indicates the number of EBS cards supported by the instance type.</p>"""
    ebs_cards: NotRequired["capo_ec2.types.ebs_card_info_list.EbsCardInfoList"]
    """<p>Describes the EBS cards available for the instance type.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EbsInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ebs_optimized_support" in value:
        import capo_ec2.types.ebs_optimized_support

        capo_ec2.types.ebs_optimized_support.serialize_ec2_query(
            value["ebs_optimized_support"], pairs, f"{key_prefix}EbsOptimizedSupport"
        )
    if "encryption_support" in value:
        import capo_ec2.types.ebs_encryption_support

        capo_ec2.types.ebs_encryption_support.serialize_ec2_query(
            value["encryption_support"], pairs, f"{key_prefix}EncryptionSupport"
        )
    if "ebs_optimized_info" in value:
        import capo_ec2.types.ebs_optimized_info

        capo_ec2.types.ebs_optimized_info.serialize_ec2_query(
            value["ebs_optimized_info"], pairs, f"{key_prefix}EbsOptimizedInfo"
        )
    if "nvme_support" in value:
        import capo_ec2.types.ebs_nvme_support

        capo_ec2.types.ebs_nvme_support.serialize_ec2_query(
            value["nvme_support"], pairs, f"{key_prefix}NvmeSupport"
        )
    if "maximum_ebs_attachments" in value:
        pairs.append(
            (
                f"{key_prefix}MaximumEbsAttachments",
                str(value["maximum_ebs_attachments"]),
            )
        )
    if "attachment_limit_type" in value:
        import capo_ec2.types.attachment_limit_type

        capo_ec2.types.attachment_limit_type.serialize_ec2_query(
            value["attachment_limit_type"], pairs, f"{key_prefix}AttachmentLimitType"
        )
    if "maximum_ebs_cards" in value:
        pairs.append((f"{key_prefix}MaximumEbsCards", str(value["maximum_ebs_cards"])))
    if "ebs_cards" in value:
        import capo_ec2.types.ebs_card_info_list

        capo_ec2.types.ebs_card_info_list.serialize_ec2_query(
            value["ebs_cards"], pairs, f"{key_prefix}EbsCardSet"
        )


def deserialize_ec2_query(el: Element) -> EbsInfo:
    out: EbsInfo = {}  # type: ignore[typeddict-item]
    child_ebs_optimized_support = el.find("ebsOptimizedSupport")
    if child_ebs_optimized_support is not None:
        import capo_ec2.types.ebs_optimized_support

        out["ebs_optimized_support"] = (
            capo_ec2.types.ebs_optimized_support.deserialize_ec2_query(
                child_ebs_optimized_support
            )
        )
    child_encryption_support = el.find("encryptionSupport")
    if child_encryption_support is not None:
        import capo_ec2.types.ebs_encryption_support

        out["encryption_support"] = (
            capo_ec2.types.ebs_encryption_support.deserialize_ec2_query(
                child_encryption_support
            )
        )
    child_ebs_optimized_info = el.find("ebsOptimizedInfo")
    if child_ebs_optimized_info is not None:
        import capo_ec2.types.ebs_optimized_info

        out["ebs_optimized_info"] = (
            capo_ec2.types.ebs_optimized_info.deserialize_ec2_query(
                child_ebs_optimized_info
            )
        )
    child_nvme_support = el.find("nvmeSupport")
    if child_nvme_support is not None:
        import capo_ec2.types.ebs_nvme_support

        out["nvme_support"] = capo_ec2.types.ebs_nvme_support.deserialize_ec2_query(
            child_nvme_support
        )
    child_maximum_ebs_attachments = el.find("maximumEbsAttachments")
    if child_maximum_ebs_attachments is not None:
        out["maximum_ebs_attachments"] = int(child_maximum_ebs_attachments.text or "")
    child_attachment_limit_type = el.find("attachmentLimitType")
    if child_attachment_limit_type is not None:
        import capo_ec2.types.attachment_limit_type

        out["attachment_limit_type"] = (
            capo_ec2.types.attachment_limit_type.deserialize_ec2_query(
                child_attachment_limit_type
            )
        )
    child_maximum_ebs_cards = el.find("maximumEbsCards")
    if child_maximum_ebs_cards is not None:
        out["maximum_ebs_cards"] = int(child_maximum_ebs_cards.text or "")
    child_ebs_cards = el.find("ebsCardSet")
    if child_ebs_cards is not None:
        import capo_ec2.types.ebs_card_info_list

        out["ebs_cards"] = capo_ec2.types.ebs_card_info_list.deserialize_ec2_query(
            child_ebs_cards
        )
    return out
