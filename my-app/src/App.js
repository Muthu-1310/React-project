
import { Layout } from 'antd';
import AppHome from './Components/views/home';
import './App.css';
import AppHeader from './Components/header';
import AppFooter from './Components/footer';

const { Header, Content, Footer } = Layout;

function App() {
  return (

    <Layout className="mainLayout">
      <Header>
        <AppHeader/>
      </Header>
      <Content>
        <AppHome/>
      </Content>
      <Footer>
        <AppFooter/>
      </Footer>
    </Layout>
  );
}

export default App;
