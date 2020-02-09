DOCUMENT_TYPES = [
    {'id': 1, 'name': 'Quyết định', 'document_type': ''},
    {'id': 2, 'name': 'Thông tư', 'document_type': ''},
    {'id': 3, 'name': 'Nghị quyết', 'document_type': ''},
    {'id': 4, 'name': 'Nghị định', 'document_type': ''},
    {'id': 5, 'name': 'Thông tư liên tịch', 'document_type': ''},
    {'id': 6, 'name': 'Luật', 'document_type': ''},
    {'id': 7, 'name': 'Lệnh', 'document_type': ''},
    {'id': 8, 'name': 'Pháp Lệnh', 'document_type': ''},
    {'id': 9, 'name': 'Chỉ thị', 'document_type': ''},
    {'id': 10, 'name': 'Nghị Quyết', 'document_type': ''}
]

DEPARTMENT_TYPES = [
    {'id': 1, 'name': 'Tài chính', 'type': ''},
    {'id': 2, 'name': 'Nội vụ', 'type': ''},
    {'id': 3, 'name': 'Nông nghiệp và phát triển nông thôn', 'type': ''},
    {'id': 4, 'name': 'Tài nguyên và Môi trường', 'type': ''},
    {'id': 5, 'name': 'Công Thương', 'type': ''},
    {'id': 6, 'name': 'GTVT', 'type': ''},
    {'id': 7, 'name': 'Lao động - Thương binh và Xã hội', 'type': ''},
    {'id': 8, 'name': 'Tư pháp', 'type': ''},
    {'id': 9, 'name': 'Giáo dục và đào tạo', 'type': ''},
    {'id': 10, 'name': 'Xây dựng', 'type': ''},
    {'id': 11, 'name': 'Kế hoạch và Đầu tư', 'type': ''},
    {'id': 12, 'name': 'Ngân hàng', 'type': ''},
    {'id': 13, 'name': 'Y tế', 'type': ''},
    {'id': 14, 'name': 'Thông tin và Truyền thông', 'type': ''},
    {'id': 15, 'name': 'Khoa học và công nghệ', 'type': ''},
    {'id': 16, 'name': 'Văn hóa Thể thao và Du lịch', 'type': ''},
    {'id': 17, 'name': 'Công an', 'type': ''},
    {'id': 18, 'name': 'Quốc phòng', 'type': ''},
    {'id': 19, 'name': 'Y tế', 'type': ''},
    {'id': 20, 'name': 'Tổ chức - Cán bộ Chính phủ', 'type': ''},
    {'id': 21, 'name': 'Văn hóa - Thông tin', 'type': ''},
    {'id': 22, 'name': 'Ngoại giao', 'type': ''},
    {'id': 23, 'name': 'Thanh tra', 'type': ''},
    {'id': 24, 'name': 'Tòa án', 'type': ''},
    {'id': 25, 'name': 'Dân tộc', 'type': ''},
    {'id': 26, 'name': 'Kiểm sát', 'type': ''},
    {'id': 27, 'name': 'Kế hoạch - Đầu tư', 'type': ''},
    {'id': 28, 'name': 'Kiểm toán', 'type': ''},
    {'id': 29, 'name': 'Công nghiệp', 'type': ''},
    {'id': 30, 'name': 'Bảo Hiểm', 'type': ''},
    {'id': 31, 'name': 'Ngành Tư pháp', 'type': ''},
    {'id': 32, 'name': 'Mặt trận Tổ quốc Việt Na', 'type': ''}
]

TOPIC_TYPES = [
    {'id': 1, 'name': 'Phí và lệ phí'},
    {'id': 2, 'name': 'Quản lý ngân sách'},
    {'id': 3, 'name': 'Quản lý thuế'},
    {'id': 4, 'name': 'Lệ phí và thu khác của ngân sách nhà nước'},
    {'id': 5, 'name': 'Đất đai'},
    {'id': 6, 'name': 'Lĩnh vực giá'},
    {'id': 7, 'name': 'Tài chính khác'},
    {'id': 8, 'name': 'Đường bộ'},
    {'id': 9, 'name': 'Ngân sách nhà nước'},
    {'id': 10, 'name': 'Tổ chức- Biên chế'},
    {'id': 11, 'name': 'Quản lý ngân sách nhà nước'},
    {'id': 12, 'name': 'TCNH và thị trường TC'},
    {'id': 13, 'name': 'Lâm nghiệp'},
    {'id': 14, 'name': 'Xuất nhập khẩu'},
    {'id': 15, 'name': 'Hàng hải'},
    {'id': 16, 'name': 'Chính quyền địa phương'},
    {'id': 17, 'name': 'Quản lý dịch vụ tài chính và các quỹ tài chính'},
    {'id': 18, 'name': 'Môi trường'},
    {'id': 19, 'name': 'Quản lý tài chính doanh nghiệp'},
    {'id': 20, 'name': 'Nông nghiệp'},
    {'id': 21, 'name': 'Tổ chức cán bộ'},
    {'id': 22, 'name': 'Chính sách thuế'},
    {'id': 23, 'name': 'Thủy sản'},
    {'id': 24, 'name': 'Phát triển nông thôn'}
]
SCOPE_TYPES = [
    {'id': 1, 'name': 'Toàn quốc'},
    {'id': 2, 'name': 'Địa phương'},
]


ES_MAPPING = {
    "id": "",
    "Tên VB" : "",
    "full_text" :"",
    "full_text_eng" : "",
    "url": "",
    "Lịch sử" : "",
    "Lược đồ" : {},
    "Thuộc tính" : {}
}

PROPERTIES_TERMS = {
    1 : "Cơ quan ban hành",
    2 : "Chức danh người ký",
    3 : "Người ký",
    4 : "Loại văn bản",
    5 : "Lí do hết hiệu lực",
    6 : "Lý do hết hiệu lực 1 phần",
    7 : "Lĩnh vực",
    8 : "Nguồn thu thập",
    9 : "Ngành",
    10 : "Ngày ban hành",
    11 : "Ngày có hiệu lực",
    12 : "Ngày hết hiệu lực",
    13 : "Ngày đăng công báo",
    14 : "Phạm vi",
    15 : "Số ký hiệu",
    16 : "Thông tin",
    17 : "Thông tin áp dụng"
}

RELATION_TERMS = {
    1 : "Văn bản HD, QĐ chi tiết",
    2 : "Văn bản bị hết hiệu lực 1 phần",
    3 : "Văn bản bị đình chỉ",
    4 : "Văn bản bổ sung",
    5 : "Văn bản căn cứ",
    6 : "Văn bản dẫn chiếu",
    7 : "Văn bản hiện thời",
    8 : "Văn bản hết hiệu lực",
    9 : "Văn bản liên quan khác",
    10 : "Văn bản quy định hết hiệu lực 1 phần",
    11 : "Văn bản sửa đổi",
    12 : "Văn bản đình chỉ",
    13 : "Văn bản đình chỉ 1 phần",
    14 : "Văn bản được HD, QĐ chi tiết",
    15 : "Văn bản được bổ sung",
    16 : "Văn bản được sửa đổi"
}

MAPPING = {
    "mappings" : {
      "properties" : {
        "Lược đồ" : {
          "properties" : {
            "Văn bản HD, QĐ chi tiết " : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản bị hết hiệu lực 1 phần " : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản bị đình chỉ" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản bổ sung" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản căn cứ" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản dẫn chiếu" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản hiện thời" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản hết hiệu lực" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản liên quan khác" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản quy định hết hiệu lực" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản quy định hết hiệu lực 1 phần " : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản sửa đổi" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản đình chỉ" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản đình chỉ 1 phần" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản được HD, QĐ chi tiết" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản được bổ sung " : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản được sửa đổi" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            }
          }
        },
        "Lịch sử" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "Thuộc tính" : {
          "properties" : {
            "Cơ quan ban hành/ Chức danh / Người ký" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Loại văn bản" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Lí do hết hiệu lực" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Lý do hết hiệu lực 1 phần" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Lĩnh vực" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Nguồn thu thập" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Ngành" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Ngày ban hành" : {
              "type" : "date",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Ngày có hiệu lực" : {
              "type" : "date",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Ngày hết hiệu lực" : {
              "type" : "date",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Ngày đăng công báo" : {
              "type" : "date",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Phạm vi" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Số ký hiệu" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Thông tin" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Thông tin áp dụng" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            }
          }
        },
        "Toàn văn" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "Tên VB" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "VB Liên Quan" : {
          "properties" : {
            "Văn bản bị bãi bỏ" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản bị bãi bỏ một phần" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản bị hết hiệu lực" : {
              "type" : "text",
              "fields" : {
                "keywordated" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản bị hủy bỏ bỏ" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản bị hủy bỏ một phần" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản bị sửa đổi" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản bị thay thế" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản bị thay thế một phần" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản bị đình chỉ" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản bị đính chính" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản căn cứ" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản dẫn chiếu" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản hết hiệu lực 1 phần" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản được hướng dẫn" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản được quy định chi tiết, hướng dẫn thi hành" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Văn bản được sửa đổi bổ sung" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            }
          }
        },
        "VB Tiếng anh" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "full_text" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "full_text_eng" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "id" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "url" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        }
      }
    }
}
