import { Table } from 'antd'
import React from 'react'

function TransTable() {
  const dataSource = [
    
  ]
  const columns = [
    {
      title: "Ngày chuyển",
      dataIndex: "date",
      key: "date"
    },
    {
      title: "Mã doc",
      dataIndex: "doc_no",
      key: "doc_no"
    },
    {
      title: "Số tiền chuyển",
      dataIndex: "amount",
      key: "amount"
    },
    {
      title: "Nội dung",
      dataIndex: "message",
      key: "message"
    },
    {
      title: "Người gửi",
      dataIndex: "sender",
      key: "sender"
    },
    {
      title: "File",
      dataIndex: "file_id",
      key: "file_id"
    },
    {
      title: "Trang",
      dataIndex: "page",
      key: "page"
    },
    
  ]
  return (
    <Table columns={columns} dataSource={dataSource}/>
  )
}

export default TransTable