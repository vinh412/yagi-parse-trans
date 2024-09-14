import {
  AutoComplete,
  Button,
  Col,
  DatePicker,
  Form,
  Input,
  InputNumber,
  Row,
  Select,
} from "antd";
import React from "react";
import dayjs from "dayjs";

const dateFormat = "DD/MM/YYYY";
function SearchForm() {
  return (
    <div>
      <Form size="large" layout="vertical">
        <Row gutter={16}>
          <Col span={8}>
            <Form.Item label="Tìm kiếm">
              <Input placeholder="Từ tìm kiếm" />
            </Form.Item>
          </Col>
          <Col span={8}>
            <Form.Item label="Khoảng thời gian">
              <DatePicker.RangePicker
                style={{width: "-webkit-fill-available"}}
                defaultValue={[
                  dayjs("01-09-2024", dateFormat),
                  dayjs("10-09-2024", dateFormat),
                ]}
                format="DD-MM-YYYY"
              />
            </Form.Item>
          </Col>
          <Col span={8}>
            <Form.Item label="Số dòng mỗi trang">
              <Select
                options={[
                  { value: 10, label: "10" },
                  { value: 20, label: "20" },
                  { value: 50, label: "50" },
                  { value: 100, label: "100" },
                  { value: 200, label: "200" },
                ]}
                defaultValue={10}
              />
            </Form.Item>
          </Col>
          <Col span={8}>
            <Form.Item label="Sắp xếp theo">
              <Select
                options={[
                  { value: "time", label: "Thời gian" },
                  { value: "amount", label: "Số tiền" },
                ]}
              />
            </Form.Item>
          </Col>
          <Col span={8}>
            <Form.Item label="Thứ tự">
              <Select
                options={[
                  { value: "ASC", label: "Tăng dần" },
                  { value: "DESC", label: "Giảm dần" },
                ]}
              />
            </Form.Item>
          </Col>
          <Col span={8}>
            <Form.Item label="Tài khoản nhận">
              <Select
                options={[
                  { value: "ASC", label: "MAT TRAN TO QUOC VN - BAN CUU TRO TW" },
                  { value: "DESC", label: "BAN VAN DONG CUU TRO TRUNG UONG" },
                ]}
              />
            </Form.Item>
          </Col>
          <Col span={24}>
            <Form.Item>
              <Button style={{width: "-webkit-fill-available"}} type="primary">Tìm kiếm</Button>
            </Form.Item>
          </Col>
        </Row>
      </Form>
    </div>
  );
}

export default SearchForm;
