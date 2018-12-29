/*
 * Generated by asn1c-0.9.28 (http://lionet.info/asn1c)
 * From ASN.1 module "MyProtocol"
 * 	found in "../../my_protocol.asn"
 * 	`asn1c -fcompound-names -fincludes-quoted -gen-PER`
 */

#include "B.h"

static asn_per_constraints_t asn_PER_type_B_constr_1 GCC_NOTUSED = {
	{ APC_CONSTRAINED,	 1,  1,  0,  1 }	/* (0..1) */,
	{ APC_UNCONSTRAINED,	-1, -1,  0,  0 },
	0, 0	/* No PER value map */
};
static asn_TYPE_member_t asn_MBR_B_1[] = {
	{ ATF_NOFLAGS, 0, offsetof(struct B, choice.a),
		(ASN_TAG_CLASS_CONTEXT | (0 << 2)),
		-1,	/* IMPLICIT tag at current level */
		&asn_DEF_C,
		0,	/* Defer constraints checking to the member type */
		0,	/* No PER visible constraints */
		0,
		"a"
		},
	{ ATF_NOFLAGS, 0, offsetof(struct B, choice.b),
		(ASN_TAG_CLASS_CONTEXT | (1 << 2)),
		-1,	/* IMPLICIT tag at current level */
		&asn_DEF_D,
		0,	/* Defer constraints checking to the member type */
		0,	/* No PER visible constraints */
		0,
		"b"
		},
};
static const asn_TYPE_tag2member_t asn_MAP_B_tag2el_1[] = {
    { (ASN_TAG_CLASS_CONTEXT | (0 << 2)), 0, 0, 0 }, /* a */
    { (ASN_TAG_CLASS_CONTEXT | (1 << 2)), 1, 0, 0 } /* b */
};
static asn_CHOICE_specifics_t asn_SPC_B_specs_1 = {
	sizeof(struct B),
	offsetof(struct B, _asn_ctx),
	offsetof(struct B, present),
	sizeof(((struct B *)0)->present),
	asn_MAP_B_tag2el_1,
	2,	/* Count of tags in the map */
	0,
	-1	/* Extensions start */
};
asn_TYPE_descriptor_t asn_DEF_B = {
	"B",
	"B",
	CHOICE_free,
	CHOICE_print,
	CHOICE_constraint,
	CHOICE_decode_ber,
	CHOICE_encode_der,
	CHOICE_decode_xer,
	CHOICE_encode_xer,
	CHOICE_decode_uper,
	CHOICE_encode_uper,
	CHOICE_outmost_tag,
	0,	/* No effective tags (pointer) */
	0,	/* No effective tags (count) */
	0,	/* No tags (pointer) */
	0,	/* No tags (count) */
	&asn_PER_type_B_constr_1,
	asn_MBR_B_1,
	2,	/* Elements count */
	&asn_SPC_B_specs_1	/* Additional specs */
};
