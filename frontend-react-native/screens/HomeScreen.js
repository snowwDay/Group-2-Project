// Home Screen 
import React from 'react'
import { SafeAreaView, StyleSheet, StatusBar, } from 'react-native'

// Structured Screen Component Imports
import HomeHeader from '../components/homeScreen/HomeHeader'
import DateHeader from '../components/homeScreen/DateHeader'
import TimeClockVersion2 from '../components/homeScreen/TimeClockVersion2'
import ScheduleViewer from '../components/homeScreen/ScheduleViewer'

// Screen 
export default function HomeScreen({ navigation }) {
    return (
        <SafeAreaView style={ styles.container }>
            <StatusBar barStyle='dark-content' />
            <HomeHeader />
            <DateHeader />
            <TimeClockVersion2 />
            <ScheduleViewer />
        </SafeAreaView>
    )
}

// Screen Style
const styles = StyleSheet.create({
    container: {
        backgroundColor: '#e4e7e4',
        flex: 1,
    },
})
