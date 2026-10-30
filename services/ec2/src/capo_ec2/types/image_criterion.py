"""Generated from Smithy shape ``com.amazonaws.ec2#ImageCriterion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.creation_date_condition
    import capo_ec2.types.deprecation_time_condition
    import capo_ec2.types.image_name_list
    import capo_ec2.types.image_provider_list
    import capo_ec2.types.image_watermark_filter_response_list
    import capo_ec2.types.marketplace_product_code_list
    import capo_ec2.types.scan_result_condition


class ImageCriterion(TypedDict, closed=True):
    image_providers: NotRequired["capo_ec2.types.image_provider_list.ImageProviderList"]
    """<p>The image providers whose images are allowed.</p> <p>Possible values:</p> <ul> <li> <p> <code>amazon</code>: Allow AMIs created by Amazon or verified providers.</p> </li> <li> <p> <code>aws-marketplace</code>: Allow AMIs created by verified providers in the Amazon Web Services Marketplace.</p> </li> <li> <p> <code>aws-backup-vault</code>: Allow AMIs created by Amazon Web Services Backup. </p> </li> <li> <p>12-digit account ID: Allow AMIs created by this account. One or more account IDs can be specified.</p> </li> <li> <p> <code>none</code>: Allow AMIs created by your own account only.</p> </li> </ul> <p>Maximum: 200 values</p>"""
    marketplace_product_codes: NotRequired[
        "capo_ec2.types.marketplace_product_code_list.MarketplaceProductCodeList"
    ]
    """<p>The Amazon Web Services Marketplace product codes for allowed images.</p> <p>Length: 1-25 characters</p> <p>Valid characters: Letters (<code>A–Z, a–z</code>) and numbers (<code>0–9</code>)</p> <p>Maximum: 50 values</p>"""
    image_names: NotRequired["capo_ec2.types.image_name_list.ImageNameList"]
    """<p>The names of allowed images. Names can include wildcards (<code>?</code> and <code>*</code>).</p> <p>Length: 1–128 characters. With <code>?</code>, the minimum is 3 characters.</p> <p>Valid characters:</p> <ul> <li> <p>Letters: <code>A–Z, a–z</code> </p> </li> <li> <p>Numbers: <code>0–9</code> </p> </li> <li> <p>Special characters: <code>( ) [ ] . / - ' @ _ * ?</code> </p> </li> <li> <p>Spaces</p> </li> </ul> <p>Maximum: 50 values</p>"""
    deprecation_time_condition: NotRequired[
        "capo_ec2.types.deprecation_time_condition.DeprecationTimeCondition"
    ]
    """<p>The maximum period since deprecation for allowed images.</p>"""
    creation_date_condition: NotRequired[
        "capo_ec2.types.creation_date_condition.CreationDateCondition"
    ]
    """<p>The maximum age for allowed images.</p>"""
    image_watermarks: NotRequired[
        "capo_ec2.types.image_watermark_filter_response_list.ImageWatermarkFilterResponseList"
    ]
    """<p>The watermark criteria that an AMI must match to be allowed. An AMI is allowed if it carries at least one watermark that satisfies an ImageWatermarkFilter. A watermark satisfies a filter when all specified fields in the ImageWatermarkFilter match the corresponding values on the watermark of the AMI.</p> <p>Maximum: 50 values</p>"""
    scan_result_condition: NotRequired[
        "capo_ec2.types.scan_result_condition.ScanResultCondition"
    ]
    """<p>The Amazon Inspector scan-result criteria that an AMI must meet to be allowed. The criteria can limit the highest finding severity, the number of days since Amazon Inspector last scanned the AMI, and the number of days since Amazon Inspector reported a fix as available.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageCriterion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "image_providers" in value:
        import capo_ec2.types.image_provider_list

        capo_ec2.types.image_provider_list.serialize_ec2_query(
            value["image_providers"], pairs, f"{key_prefix}ImageProviderSet"
        )
    if "marketplace_product_codes" in value:
        import capo_ec2.types.marketplace_product_code_list

        capo_ec2.types.marketplace_product_code_list.serialize_ec2_query(
            value["marketplace_product_codes"],
            pairs,
            f"{key_prefix}MarketplaceProductCodeSet",
        )
    if "image_names" in value:
        import capo_ec2.types.image_name_list

        capo_ec2.types.image_name_list.serialize_ec2_query(
            value["image_names"], pairs, f"{key_prefix}ImageNameSet"
        )
    if "deprecation_time_condition" in value:
        import capo_ec2.types.deprecation_time_condition

        capo_ec2.types.deprecation_time_condition.serialize_ec2_query(
            value["deprecation_time_condition"],
            pairs,
            f"{key_prefix}DeprecationTimeCondition",
        )
    if "creation_date_condition" in value:
        import capo_ec2.types.creation_date_condition

        capo_ec2.types.creation_date_condition.serialize_ec2_query(
            value["creation_date_condition"],
            pairs,
            f"{key_prefix}CreationDateCondition",
        )
    if "image_watermarks" in value:
        import capo_ec2.types.image_watermark_filter_response_list

        capo_ec2.types.image_watermark_filter_response_list.serialize_ec2_query(
            value["image_watermarks"], pairs, f"{key_prefix}ImageWatermarkSet"
        )
    if "scan_result_condition" in value:
        import capo_ec2.types.scan_result_condition

        capo_ec2.types.scan_result_condition.serialize_ec2_query(
            value["scan_result_condition"], pairs, f"{key_prefix}ScanResultCondition"
        )


def deserialize_ec2_query(el: Element) -> ImageCriterion:
    out: ImageCriterion = {}  # type: ignore[typeddict-item]
    child_image_providers = el.find("imageProviderSet")
    if child_image_providers is not None:
        import capo_ec2.types.image_provider_list

        out["image_providers"] = (
            capo_ec2.types.image_provider_list.deserialize_ec2_query(
                child_image_providers
            )
        )
    child_marketplace_product_codes = el.find("marketplaceProductCodeSet")
    if child_marketplace_product_codes is not None:
        import capo_ec2.types.marketplace_product_code_list

        out["marketplace_product_codes"] = (
            capo_ec2.types.marketplace_product_code_list.deserialize_ec2_query(
                child_marketplace_product_codes
            )
        )
    child_image_names = el.find("imageNameSet")
    if child_image_names is not None:
        import capo_ec2.types.image_name_list

        out["image_names"] = capo_ec2.types.image_name_list.deserialize_ec2_query(
            child_image_names
        )
    child_deprecation_time_condition = el.find("deprecationTimeCondition")
    if child_deprecation_time_condition is not None:
        import capo_ec2.types.deprecation_time_condition

        out["deprecation_time_condition"] = (
            capo_ec2.types.deprecation_time_condition.deserialize_ec2_query(
                child_deprecation_time_condition
            )
        )
    child_creation_date_condition = el.find("creationDateCondition")
    if child_creation_date_condition is not None:
        import capo_ec2.types.creation_date_condition

        out["creation_date_condition"] = (
            capo_ec2.types.creation_date_condition.deserialize_ec2_query(
                child_creation_date_condition
            )
        )
    child_image_watermarks = el.find("imageWatermarkSet")
    if child_image_watermarks is not None:
        import capo_ec2.types.image_watermark_filter_response_list

        out["image_watermarks"] = (
            capo_ec2.types.image_watermark_filter_response_list.deserialize_ec2_query(
                child_image_watermarks
            )
        )
    child_scan_result_condition = el.find("scanResultCondition")
    if child_scan_result_condition is not None:
        import capo_ec2.types.scan_result_condition

        out["scan_result_condition"] = (
            capo_ec2.types.scan_result_condition.deserialize_ec2_query(
                child_scan_result_condition
            )
        )
    return out
