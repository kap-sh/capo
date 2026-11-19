"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#SearchAgreementsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.catalog
    import capo_marketplace_agreement.types.filter_list
    import capo_marketplace_agreement.types.max_results
    import capo_marketplace_agreement.types.next_token
    import capo_marketplace_agreement.types.sort


class SearchAgreementsInput(TypedDict, closed=True):
    catalog: NotRequired["capo_marketplace_agreement.types.catalog.Catalog"]
    """<p>The catalog in which the agreement was created.</p>"""
    filters: NotRequired["capo_marketplace_agreement.types.filter_list.FilterList"]
    """<p>The filter name and value pair used to return a specific list of results.</p> <p>The following filters are supported:</p> <ul> <li> <p> <code>ResourceIdentifier</code> – The unique identifier of the resource.</p> </li> <li> <p> <code>ResourceType</code> – Type of the resource, which is the product (<code>AmiProduct</code>, <code>ContainerProduct</code>, <code>SaaSProduct</code>, <code>ProfessionalServicesProduct</code>, or <code>MachineLearningProduct</code>).</p> </li> <li> <p> <code>PartyType</code> – The party type of the caller. Use <code>Proposer</code> or <code>Acceptor</code>.</p> </li> <li> <p> <code>AcceptorAccountId</code> – The AWS account ID of the party accepting the agreement terms.</p> </li> <li> <p> <code>OfferId</code> – The unique identifier of the offer in which the terms are registered in the agreement token.</p> </li> <li> <p> <code>Status</code> – The current status of the agreement. Values include <code>ACTIVE</code>, <code>CANCELLED</code>, <code>EXPIRED</code>, <code>RENEWED</code>, <code>REPLACED</code>, and <code>TERMINATED</code>.</p> </li> <li> <p> <code>BeforeEndTime</code> – A date used to filter agreements with a date before the <code>endTime</code> of an agreement.</p> </li> <li> <p> <code>AfterEndTime</code> – A date used to filter agreements with a date after the <code>endTime</code> of an agreement.</p> </li> <li> <p> <code>BeforeStartTime</code> – A date used to filter agreements with a date before the <code>startTime</code> of an agreement.</p> </li> <li> <p> <code>AfterStartTime</code> – A date used to filter agreements with a date after the <code>startTime</code> of an agreement.</p> </li> <li> <p> <code>BeforeLastUpdateTime</code> – A date used to filter agreements with a date before the <code>lastUpdateTime</code> of an agreement.</p> </li> <li> <p> <code>AfterLastUpdateTime</code> – A date used to filter agreements with a date after the <code>lastUpdateTime</code> of an agreement.</p> </li> <li> <p> <code>AgreementType</code> – The type of agreement. Supported value includes <code>PurchaseAgreement</code>.</p> </li> <li> <p> <code>OfferSetId</code> – A unique identifier for the offer set containing this offer. All agreements created from offers in this set include this identifier as context.</p> </li> <li> <p> <code>EndTimeBehaviorType</code> – What happens to the agreement when it reaches its end date. Values include <code>RENEW</code>, <code>REPLACE</code>, and <code>EXPIRE</code>.</p> </li> <li> <p> <code>EndTimeBehaviorReasonCode</code> – The reason why the agreement doesn't renew at its end date. Values include <code>PROPOSER_RENEW_OPTED_OUT</code>, <code>ACCEPTOR_RENEW_OPTED_OUT</code>, <code>NO_RENEWAL_TERM</code>, and <code>RENEWAL_LIMIT_EXHAUSTED</code>.</p> </li> <li> <p> <code>InitialAgreementId</code> – The unique identifier of the very first agreement in a chain of related agreements. Use this filter to return every agreement in the same chain.</p> </li> <li> <p> <code>LicenseArn</code> – The Amazon Resource Name (ARN) of the AWS License Manager license associated with an entitlement granted by the agreement.</p> </li> <li> <p> <code>IncludesContactOfType</code> – The type of contact information on file for the agreement. Supported value includes <code>ACCEPTOR</code>.</p> </li> </ul> <p>A proposer can use any combination of the preceding filters along with <code>AgreementType</code>, which is required.</p> <p>The following filter combinations are supported when the <code>PartyType</code> is <code>Acceptor</code>:</p> <ul> <li> <p> <code>AgreementType</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>Status</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>EndTime</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>Status</code> + <code>EndTime</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>ResourceIdentifier</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>ResourceIdentifier</code> + <code>EndTime</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>ResourceIdentifier</code> + <code>Status</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>ResourceIdentifier</code> + <code>Status</code> + <code>EndTime</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>ResourceType</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>ResourceType</code> + <code>EndTime</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>OfferId</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>OfferId</code> + <code>EndTime</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>OfferId</code> + <code>Status</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>OfferId</code> + <code>Status</code> + <code>EndTime</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>OfferSetId</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>OfferSetId</code> + <code>EndTime</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>OfferSetId</code> + <code>Status</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>OfferSetId</code> + <code>Status</code> + <code>EndTime</code> </p> </li> </ul> <note> <p>To filter by <code>EndTime</code>, you can use <code>BeforeEndTime</code>, <code>AfterEndTime</code>, or both.</p> </note>"""
    sort: NotRequired["capo_marketplace_agreement.types.sort.Sort"]
    """<p>An object that contains the <code>SortBy</code> and <code>SortOrder</code> attributes. For <code>SearchAgreements</code>, <code>SortBy</code> supports <code>EndTime</code> for both party types, and <code>StartTime</code> and <code>LastUpdateTime</code> only when <code>PartyType</code> is <code>Proposer</code>. The default <code>SortBy</code> value is <code>EndTime</code>.</p>"""
    max_results: NotRequired["capo_marketplace_agreement.types.max_results.MaxResults"]
    """<p>The maximum number of agreements to return in the response.</p>"""
    next_token: NotRequired["capo_marketplace_agreement.types.next_token.NextToken"]
    """<p>A token to specify where to start pagination.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchAgreementsInput) -> dict:
    out: dict = {}
    if "catalog" in value:
        out["catalog"] = value["catalog"]
    if "filters" in value:
        import capo_marketplace_agreement.types.filter_list

        out["filters"] = (
            capo_marketplace_agreement.types.filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "sort" in value:
        import capo_marketplace_agreement.types.sort

        out["sort"] = capo_marketplace_agreement.types.sort.serialize_aws_json_1_0(
            value["sort"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SearchAgreementsInput:
    out: SearchAgreementsInput = {}  # type: ignore[typeddict-item]
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    if data.get("filters") is not None:
        import capo_marketplace_agreement.types.filter_list

        out["filters"] = (
            capo_marketplace_agreement.types.filter_list.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if data.get("sort") is not None:
        import capo_marketplace_agreement.types.sort

        out["sort"] = capo_marketplace_agreement.types.sort.deserialize_aws_json_1_0(
            data["sort"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SearchAgreementsInput) -> dict:
    out: dict = {}
    if "catalog" in value:
        out["catalog"] = value["catalog"]
    if "filters" in value:
        import capo_marketplace_agreement.types.filter_list

        out["filters"] = capo_marketplace_agreement.types.filter_list.serialize_cbor(
            value["filters"]
        )
    if "sort" in value:
        import capo_marketplace_agreement.types.sort

        out["sort"] = capo_marketplace_agreement.types.sort.serialize_cbor(
            value["sort"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> SearchAgreementsInput:
    out: SearchAgreementsInput = {}  # type: ignore[typeddict-item]
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    if data.get("filters") is not None:
        import capo_marketplace_agreement.types.filter_list

        out["filters"] = capo_marketplace_agreement.types.filter_list.deserialize_cbor(
            data["filters"]
        )
    if data.get("sort") is not None:
        import capo_marketplace_agreement.types.sort

        out["sort"] = capo_marketplace_agreement.types.sort.deserialize_cbor(
            data["sort"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
