# Copyright 2013, Big Switch Networks, Inc.
#
# LoxiGen is licensed under the Eclipse Public License, version 1.0 (EPL), with
# the following special exception:
#
# LOXI Exception
#
# As a special exception to the terms of the EPL, you may distribute libraries
# generated by LoxiGen (LoxiGen Libraries) under the terms of your choice, provided
# that copyright and licensing notices generated by LoxiGen are not altered or removed
# from the LoxiGen Libraries and the notice provided below is (i) included in
# the LoxiGen Libraries, if distributed in source code form and (ii) included in any
# documentation for the LoxiGen Libraries, if distributed in binary form.
#
# Notice: "Copyright 2013, Big Switch Networks, Inc. This library was generated by the LoxiGen Compiler."
#
# You may not use this file except in compliance with the EPL or LOXI Exception. You may obtain
# a copy of the EPL at:
#
# http://www.eclipse.org/legal/epl-v10.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# EPL for the specific language governing permissions and limitations
# under the EPL.

# Map from LOXI types to Wireshark types
oftype_to_wireshark_type = {
    "char": "INT8",
    "uint8_t": "UINT8",
    "uint16_t": "UINT16",
    "uint32_t": "UINT32",
    "uint64_t": "UINT64",
    "of_mac_addr_t": "ETHER",
    "of_ipv4_t": "IPv4",
    "of_ipv6_t": "IPv6",
    "of_port_name_t": "STRINGZ",
    "of_table_name_t": "STRINGZ",
    "of_desc_str_t": "STRINGZ",
    "of_serial_num_t": "STRINGZ",
    "of_octets_t": "BYTES",
    "of_port_no_t": "UINT32",
    "of_port_desc_t": "STRINGZ",
    "of_bsn_vport_t": "BYTES",
    "of_bsn_vport_q_in_q_t": "BYTES",
    "of_fm_cmd_t": "UINT16",
    "of_wc_bmap_t": "UINT64",
    "of_match_bmap_t": "UINT64",
    "of_match_t": "BYTES",
    "of_oxm_t": "BYTES",
    "of_meter_features_t": "BYTES",
}

# Map from LOXI type to Wireshark base
oftype_to_base = {
    "char": "DEC",
    "uint8_t": "DEC",
    "uint16_t": "DEC",
    "uint32_t": "DEC",
    "uint64_t": "DEC",
    "of_mac_addr_t": "NONE",
    "of_ipv4_t": "NONE",
    "of_ipv6_t": "NONE",
    "of_port_name_t": "NONE",
    "of_table_name_t": "NONE",
    "of_desc_str_t": "NONE",
    "of_serial_num_t": "NONE",
    "of_octets_t": "NONE",
    "of_port_no_t": "DEC",
    "of_port_desc_t": "NONE",
    "of_bsn_vport_t": "NONE",
    "of_bsn_vport_q_in_q_t": "NONE",
    "of_fm_cmd_t": "DEC",
    "of_wc_bmap_t": "HEX",
    "of_match_bmap_t": "HEX",
    "of_match_t": "NONE",
    "of_oxm_t": "NONE",
    "of_meter_features_t": "NONE",
}

# Override oftype_to_base for certain field names
field_to_base = {
    "eth_type": "HEX",
    "cookie": "HEX",
    "datapath_id": "HEX",
}
