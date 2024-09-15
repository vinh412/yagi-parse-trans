import React from 'react';
import { Layout, theme, Typography } from 'antd';
import HomePage from './HomePage';
const { Header, Content, Footer } = Layout;

const MyLayout = () => {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();
  return (
    <Layout>
      <Header
        style={{
          background: colorBgContainer,
          position: 'sticky',
          top: 0,
          zIndex: 1,
          width: '100%',
          display: 'flex',
          alignItems: 'center',
          marginBottom: "24px"
        }}
      >
        <Typography.Title level={2}>Sao kê Yagi</Typography.Title>
      </Header>
      <Content
        style={{
          padding: '0 48px',
        }}
      >
        <div
          style={{
            padding: 24,
            minHeight: 600,
            background: colorBgContainer,
            borderRadius: borderRadiusLG,
          }}
        >
          <HomePage />
        </div>
      </Content>
      <Footer
        style={{
          textAlign: 'center',
        }}
      >
        ©{new Date().getFullYear()} Made by vinhdd
      </Footer>
    </Layout>
  );
};
export default MyLayout;