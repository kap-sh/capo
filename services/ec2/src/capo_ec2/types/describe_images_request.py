"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.executable_by_string_list
    import capo_ec2.types.filter_list
    import capo_ec2.types.image_id_string_list
    import capo_ec2.types.integer
    import capo_ec2.types.owner_string_list
    import capo_ec2.types.string


class DescribeImagesRequest(TypedDict, closed=True):
    executable_users: NotRequired[
        "capo_ec2.types.executable_by_string_list.ExecutableByStringList"
    ]
    """<p>Scopes the images by users with explicit launch permissions. Specify an Amazon Web Services account ID, <code>self</code> (the sender of the request), or <code>all</code> (public AMIs).</p> <ul> <li> <p>If you specify an Amazon Web Services account ID that is not your own, only AMIs shared with that specific Amazon Web Services account ID are returned. However, AMIs that are shared with the account’s organization or organizational unit (OU) are not returned.</p> </li> <li> <p>If you specify <code>self</code> or your own Amazon Web Services account ID, AMIs shared with your account are returned. In addition, AMIs that are shared with the organization or OU of which you are member are also returned. </p> </li> <li> <p>If you specify <code>all</code>, all public AMIs are returned.</p> </li> </ul>"""
    image_ids: NotRequired["capo_ec2.types.image_id_string_list.ImageIdStringList"]
    """<p>The image IDs.</p> <p>Default: Describes all images available to you.</p>"""
    owners: NotRequired["capo_ec2.types.owner_string_list.OwnerStringList"]
    """<p>Scopes the results to images with the specified owners. You can specify a combination of Amazon Web Services account IDs, <code>self</code>, <code>amazon</code>, <code>aws-backup-vault</code>, and <code>aws-marketplace</code>. If you omit this parameter, the results include all images for which you have launch permissions, regardless of ownership.</p>"""
    include_deprecated: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to include deprecated AMIs.</p> <p>Default: No deprecated AMIs are included in the response.</p> <note> <p>If you are the AMI owner, all deprecated AMIs appear in the response regardless of what you specify for this parameter.</p> </note>"""
    include_disabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to include disabled AMIs.</p> <p>Default: No disabled AMIs are included in the response.</p>"""
    max_results: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>architecture</code> - The image architecture (<code>i386</code> | <code>x86_64</code> | <code>arm64</code> | <code>x86_64_mac</code> | <code>arm64_mac</code>).</p> </li> <li> <p> <code>block-device-mapping.delete-on-termination</code> - A Boolean value that indicates whether the Amazon EBS volume is deleted on instance termination.</p> </li> <li> <p> <code>block-device-mapping.device-name</code> - The device name specified in the block device mapping (for example, <code>/dev/sdh</code> or <code>xvdh</code>).</p> </li> <li> <p> <code>block-device-mapping.snapshot-id</code> - The ID of the snapshot used for the Amazon EBS volume.</p> </li> <li> <p> <code>block-device-mapping.volume-size</code> - The volume size of the Amazon EBS volume, in GiB.</p> </li> <li> <p> <code>block-device-mapping.volume-type</code> - The volume type of the Amazon EBS volume (<code>io1</code> | <code>io2</code> | <code>gp2</code> | <code>gp3</code> | <code>sc1 </code>| <code>st1</code> | <code>standard</code>).</p> </li> <li> <p> <code>block-device-mapping.encrypted</code> - A Boolean that indicates whether the Amazon EBS volume is encrypted.</p> </li> <li> <p> <code>boot-mode</code> – The boot mode of the image (<code>legacy-bios</code> | <code>uefi</code> | <code>uefi-preferred</code>).</p> </li> <li> <p> <code>creation-date</code> - The time when the image was created, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), for example, <code>2021-09-29T11:04:43.305Z</code>. You can use a wildcard (<code>*</code>), for example, <code>2021-09-29T*</code>, which matches an entire day.</p> </li> <li> <p> <code>description</code> - The description of the image (provided during image creation).</p> </li> <li> <p> <code>ena-support</code> - A Boolean that indicates whether enhanced networking with ENA is enabled.</p> </li> <li> <p> <code>free-tier-eligible</code> - A Boolean that indicates whether this image can be used under the Amazon Web Services Free Tier (<code>true</code> | <code>false</code>).</p> </li> <li> <p> <code>hypervisor</code> - The hypervisor type (<code>ovm</code> | <code>xen</code>).</p> </li> <li> <p> <code>image-allowed</code> - A Boolean that indicates whether the image meets the criteria specified for Allowed AMIs.</p> </li> <li> <p> <code>image-id</code> - The ID of the image.</p> </li> <li> <p> <code>image-watermark.source-image-creation-time</code> - The creation date of the source AMI, in the ISO 8601 format in the UTC time zone (<code> <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>.<i>ssssss</i>+<i>HH</i>:<i>MM</i> </code>). You can use a wildcard (<code>*</code>), for example, <code>2021-09-29T*</code>, which matches an entire day.</p> </li> <li> <p> <code>image-watermark.source-image-id</code> - The ID of the AMI to which the watermark was originally attached.</p> </li> <li> <p> <code>image-watermark.source-image-region</code> - The Region where the watermark was originally attached.</p> </li> <li> <p> <code>image-watermark.watermark-creation-time</code> - The date and time the watermark was attached to the AMI, in the ISO 8601 format in the UTC time zone (<code> <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>.<i>ssssss</i>+<i>HH</i>:<i>MM</i> </code>). You can use a wildcard (<code>*</code>), for example, <code>2021-09-29T*</code>, which matches an entire day.</p> </li> <li> <p> <code>image-watermark.watermark-key</code> - The watermark identifier, in <code>accountId:watermarkName</code> format (for example, <code>123456789012:approvedAmi</code>).</p> </li> <li> <p> <code>image-type</code> - The image type (<code>machine</code> | <code>kernel</code> | <code>ramdisk</code>).</p> </li> <li> <p> <code>instance-type-specification.supported-instance-type</code> – The instance types that are compatible with the AMI, as specified by the AMI owner. Values can be individual instance types (for example, <code>t3.micro</code>) or wildcard patterns that match multiple instance types (for example, <code>t3.*</code>).</p> </li> <li> <p> <code>instance-type-specification.unsupported-instance-type</code> – The instance types that are not compatible with the AMI, as specified by the AMI owner. Values can be individual instance types (for example, <code>t3.micro</code>) or wildcard patterns that match multiple instance types (for example, <code>t3.*</code>).</p> </li> <li> <p> <code>is-public</code> - A Boolean that indicates whether the image is public.</p> </li> <li> <p> <code>kernel-id</code> - The kernel ID.</p> </li> <li> <p> <code>manifest-location</code> - The location of the image manifest.</p> </li> <li> <p> <code>name</code> - The name of the AMI (provided during image creation).</p> </li> <li> <p> <code>owner-alias</code> - The owner alias (<code>amazon</code> | <code>aws-backup-vault</code> | <code>aws-marketplace</code>). The valid aliases are defined in an Amazon-maintained list. This is not the Amazon Web Services account alias that can be set using the IAM console. We recommend that you use the <b>Owner</b> request parameter instead of this filter.</p> </li> <li> <p> <code>owner-id</code> - The Amazon Web Services account ID of the owner. We recommend that you use the <b>Owner</b> request parameter instead of this filter.</p> </li> <li> <p> <code>platform</code> - The platform. The only supported value is <code>windows</code>.</p> </li> <li> <p> <code>product-code</code> - The product code.</p> </li> <li> <p> <code>product-code.type</code> - The type of the product code (<code>marketplace</code>).</p> </li> <li> <p> <code>public-ssm-parameter-name</code> - The name of a public Systems Manager parameter associated with the AMI. The parameter must be in a trusted Amazon Web Services namespace under <code>aws/service/</code>. Returns all AMIs that have ever been associated with the parameter, including previous versions.</p> </li> <li> <p> <code>ramdisk-id</code> - The RAM disk ID.</p> </li> <li> <p> <code>root-device-name</code> - The device name of the root device volume (for example, <code>/dev/sda1</code>).</p> </li> <li> <p> <code>root-device-type</code> - The type of the root device volume (<code>ebs</code> | <code>instance-store</code>).</p> </li> <li> <p> <code>source-image-id</code> - The ID of the source AMI from which the AMI was created.</p> </li> <li> <p> <code>source-image-region</code> - The Region of the source AMI.</p> </li> <li> <p> <code>source-instance-id</code> - The ID of the instance that the AMI was created from if the AMI was created using CreateImage. This filter is applicable only if the AMI was created using <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html">CreateImage</a>.</p> </li> <li> <p> <code>state</code> - The state of the image (<code>available</code> | <code>pending</code> | <code>failed</code>).</p> </li> <li> <p> <code>state-reason-code</code> - The reason code for the state change.</p> </li> <li> <p> <code>state-reason-message</code> - The message for the state change.</p> </li> <li> <p> <code>sriov-net-support</code> - A value of <code>simple</code> indicates that enhanced networking with the Intel 82599 VF interface is enabled.</p> </li> <li> <p> <code>tag:<key></code> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>virtualization-type</code> - The virtualization type (<code>paravirtual</code> | <code>hvm</code>).</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeImagesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "executable_users" in value:
        import capo_ec2.types.executable_by_string_list

        capo_ec2.types.executable_by_string_list.serialize_ec2_query(
            value["executable_users"], pairs, f"{key_prefix}ExecutableBy"
        )
    if "image_ids" in value:
        import capo_ec2.types.image_id_string_list

        capo_ec2.types.image_id_string_list.serialize_ec2_query(
            value["image_ids"], pairs, f"{key_prefix}ImageId"
        )
    if "owners" in value:
        import capo_ec2.types.owner_string_list

        capo_ec2.types.owner_string_list.serialize_ec2_query(
            value["owners"], pairs, f"{key_prefix}Owner"
        )
    if "include_deprecated" in value:
        pairs.append(
            (
                f"{key_prefix}IncludeDeprecated",
                "true" if value["include_deprecated"] else "false",
            )
        )
    if "include_disabled" in value:
        pairs.append(
            (
                f"{key_prefix}IncludeDisabled",
                "true" if value["include_disabled"] else "false",
            )
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )


def deserialize_ec2_query(el: Element) -> DescribeImagesRequest:
    out: DescribeImagesRequest = {}  # type: ignore[typeddict-item]
    child_executable_users = el.find("ExecutableBy")
    if child_executable_users is not None:
        import capo_ec2.types.executable_by_string_list

        out["executable_users"] = (
            capo_ec2.types.executable_by_string_list.deserialize_ec2_query(
                child_executable_users
            )
        )
    child_image_ids = el.find("ImageId")
    if child_image_ids is not None:
        import capo_ec2.types.image_id_string_list

        out["image_ids"] = capo_ec2.types.image_id_string_list.deserialize_ec2_query(
            child_image_ids
        )
    child_owners = el.find("Owner")
    if child_owners is not None:
        import capo_ec2.types.owner_string_list

        out["owners"] = capo_ec2.types.owner_string_list.deserialize_ec2_query(
            child_owners
        )
    child_include_deprecated = el.find("IncludeDeprecated")
    if child_include_deprecated is not None:
        out["include_deprecated"] = (
            child_include_deprecated.text or ""
        ).lower() == "true"
    child_include_disabled = el.find("IncludeDisabled")
    if child_include_disabled is not None:
        out["include_disabled"] = (child_include_disabled.text or "").lower() == "true"
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    return out
