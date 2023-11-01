import {ImageSourcePropType} from 'react-native';
import styled from 'styled-components/native';

const SplashIcon = (props: {source: ImageSourcePropType}) => {
  const StyledIcon = styled.Image`
    margin: auto;
    height: 150px;
    margin: 0px 0 30px 0;
    width: 150px;
  `;
  return <StyledIcon source={props.source} />;
};

SplashIcon.defaultProps = {
  source: require('../../assets/images/chef_hat.png'),
};

export default SplashIcon;
