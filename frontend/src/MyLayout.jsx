import React from 'react';
import { Breadcrumb, Layout, Menu, theme } from 'antd';
import TransTable from './TransTable';
import SearchForm from './SearchForm';
const { Header, Content, Footer } = Layout;

const MyLayout = () => {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();
  return (
    <Layout>
      <Header
        style={{
          position: 'sticky',
          top: 0,
          zIndex: 1,
          width: '100%',
          display: 'flex',
          alignItems: 'center',
        }}
      >
        <div className="demo-logo" />
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
          <SearchForm />
          <TransTable />
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