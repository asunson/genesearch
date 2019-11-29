import React from 'react';
import {configure, mount} from 'enzyme';
import {TopBar} from '../../layouts/TopBar'
import Adapter from 'enzyme-adapter-react-16';

configure({ adapter: new Adapter() });

describe('TopBar', () => {
    let component;

    beforeEach(() => {
        component = mount(
            <TopBar/>
        )
    });

    it('should render the title text', () => {
        expect(component.find("h5").text()).toContain("GeneSearch")
    });
});